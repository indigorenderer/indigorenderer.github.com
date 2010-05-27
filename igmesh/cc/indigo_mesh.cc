// Copyright (c) 2008-2010 Glare Technologies Limited. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found at http://www.indigorenderer.com/opensource/licence.txt
//
//

#include "indigo_mesh.h"
#include <fstream>
#include <limits>


namespace Indigo
{


IndigoMesh::IndigoMesh()
{
}


IndigoMesh::~IndigoMesh()
{
}


static const uint32 MAX_STRING_LENGTH = 1024;
static const uint32 MAX_VECTOR_LENGTH = std::numeric_limits<uint32>::max();
static const uint32 MAGIC_NUMBER = 5456751;
static const uint32 FORMAT_VERSION = 1;


template <class T>
inline static void writeBasic(std::ostream& stream, const T& t)
{
	stream.write((const char*)&t, sizeof(T));
}


template <class T>
inline static void readBasic(std::istream& stream, T& t_out)
{
	stream.read((char*)&t_out, sizeof(T));
}


inline static void write(std::ostream& stream, float x)
{
	writeBasic(stream, x);
}


inline static void read(std::istream& stream, float& x)
{
	readBasic(stream, x);
}


static void write(std::ostream& stream, const std::string& s)
{
	const uint32 len = s.length();
	if(len > MAX_STRING_LENGTH)
		throw IndigoMeshExcep("String too long.");

	writeBasic(stream, len);

	stream.write(s.c_str(), len);
}


static void read(std::istream& stream, std::string& s_out)
{
	uint32 len;
	readBasic(stream, len);
	if(len > MAX_STRING_LENGTH)
		throw IndigoMeshExcep("String too long.");

	char buf[MAX_STRING_LENGTH];
	stream.read(buf, len);

	s_out = std::string(buf, len);
}


static void write(std::ostream& s, const UVSetExposition& x)
{
	write(s, x.uv_set_name);
	writeBasic(s, x.uv_set_index);
}


static void read(std::istream& s, UVSetExposition& x)
{
	read(s, x.uv_set_name);
	readBasic(s, x.uv_set_index);
}


static void write(std::ostream& s, const Vec2f& x)
{
	writeBasic(s, x);
}


static void read(std::istream& s, Vec2f& x)
{
	readBasic(s, x);
}


static void write(std::ostream& s, const Vec3f& x)
{
	writeBasic(s, x);
}


static void read(std::istream& s, Vec3f& x)
{
	readBasic(s, x);
}


static void write(std::ostream& s, const Triangle& x)
{
	writeBasic(s, x);
}


static void read(std::istream& s, Triangle& x)
{
	readBasic(s, x);
}


template <class T>
static void writeVector(std::ostream& stream, const std::vector<T>& v)
{
	if(v.size() > (std::vector<T>::size_type)MAX_VECTOR_LENGTH)
		throw IndigoMeshExcep("Vector too long.");

	const uint32 len = (uint32)v.size();
	writeBasic(stream, len);

	for(uint32 i=0; i<v.size(); ++i)
		write(stream, v[i]);
}


template <class T>
static void readVector(std::istream& stream, std::vector<T>& v_out)
{
	uint32 len;
	readBasic(stream, len);

	v_out.resize(len);

	for(uint32 i=0; i<len; ++i)
		read(stream, v_out[i]);
}


void IndigoMesh::writeToFile(const std::string& dest_path, const IndigoMesh& mesh) // throws IndigoMeshExcep on failure
{
	if(mesh.num_uv_mappings > 0 && (mesh.uv_pairs.size() % mesh.num_uv_mappings != 0))
		throw IndigoMeshExcep("Mesh uv_pairs.size() must be a multiple of mesh.num_uv_mappings");

	if(mesh.vert_normals.size() != 0 && (mesh.vert_normals.size() != mesh.vert_positions.size()))
		throw IndigoMeshExcep("Must be zero normals, or normals.size() must equal verts.size()");

	std::ofstream file(dest_path.c_str(), std::ios_base::out | std::ios_base::binary);

	if(!file)
		throw IndigoMeshExcep("Failed to open file '" + dest_path + "' for writing.");

	writeBasic(file, MAGIC_NUMBER);
	writeBasic(file, FORMAT_VERSION);
	writeBasic(file, mesh.num_uv_mappings);

	writeVector(file, mesh.used_materials);
	writeVector(file, mesh.uv_set_expositions);
	writeVector(file, mesh.vert_positions);
	writeVector(file, mesh.vert_normals);
	writeVector(file, mesh.uv_pairs);
	writeVector(file, mesh.triangles);

	if(!file)
		throw IndigoMeshExcep("Error while writing to '" + dest_path + "'.");
}


void IndigoMesh::readFromFile(const std::string& src_path, IndigoMesh& mesh_out) // throws IndigoMeshExcep on failure
{
	try
	{
		std::ifstream file(src_path.c_str(), std::ios_base::in | std::ios_base::binary);

		if(!file)
			throw IndigoMeshExcep("Failed to open file '" + src_path + "' for reading.");

		uint32 magic_number;
		readBasic(file, magic_number);
		if(magic_number != MAGIC_NUMBER)
			throw IndigoMeshExcep("Invalid magic number.");

		uint32 format_version;
		readBasic(file, format_version);
		if(format_version != FORMAT_VERSION)
			throw IndigoMeshExcep("Invalid format version.");

		readBasic(file, mesh_out.num_uv_mappings);
		
		readVector(file, mesh_out.used_materials);
		readVector(file, mesh_out.uv_set_expositions);
		readVector(file, mesh_out.vert_positions);
		readVector(file, mesh_out.vert_normals);
		readVector(file, mesh_out.uv_pairs);
		readVector(file, mesh_out.triangles);

		if(!file)
			throw IndigoMeshExcep("Error while reading from '" + src_path + "'.");

		if(mesh_out.num_uv_mappings > 0 && (mesh_out.uv_pairs.size() % mesh_out.num_uv_mappings != 0))
			throw IndigoMeshExcep("Mesh uv_pairs.size() must be a multiple of mesh.num_uv_mappings");

		if(mesh_out.vert_normals.size() != 0 && (mesh_out.vert_normals.size() != mesh_out.vert_positions.size()))
			throw IndigoMeshExcep("Must be zero normals, or normals.size() must equal verts.size()");
	}
	catch(std::bad_alloc&)
	{
		throw IndigoMeshExcep("Bad allocation while reading from file.");
	}
}


}
