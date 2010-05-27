// Copyright (c) 2008-2010 Glare Technologies Limited. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found at http://www.indigorenderer.com/opensource/licence.txt
//
//

#ifndef INDIGO_INDIGOMESH_H
#define INDIGO_INDIGOMESH_H


#include <vector>
#include <string>
#include <exception>


namespace Indigo
{


typedef unsigned int uint32;


class Vec2f
{
public:
	inline Vec2f() {}
	inline Vec2f(float x_, float y_) : x(x_), y(y_) {}
	float x, y;
};


class Vec3f
{
public:
	inline Vec3f() {}
	inline Vec3f(float x_, float y_, float z_) : x(x_), y(y_), z(z_) {}
	float x, y, z;
};


class Triangle
{
public:
	uint32 vertex_indices[3];
	uint32 uv_indices[3];
	uint32 tri_mat_index;
};


class UVSetExposition
{
public:
	UVSetExposition() {}
	UVSetExposition(const std::string& n, uint32 i) : uv_set_name(n), uv_set_index(i) {}
	std::string uv_set_name;
	uint32 uv_set_index;
};


class IndigoMeshExcep : public std::exception
{
public:
	IndigoMeshExcep(const std::string& m) : std::exception(m.c_str()) {}
};


/*=====================================================================
IndigoMesh
----------

=====================================================================*/
class IndigoMesh
{
public:
	/*=====================================================================
	IndigoMesh
	----------
	
	=====================================================================*/
	IndigoMesh();

	~IndigoMesh();

	static void writeToFile(const std::string& dest_path, const IndigoMesh& mesh); // throws IndigoMeshExcep on failure
	static void readFromFile(const std::string& src_path, IndigoMesh& mesh_out); // throws IndigoMeshExcep on failure


	uint32 num_uv_mappings;
	
	std::vector<std::string> used_materials;

	std::vector<UVSetExposition> uv_set_expositions;

	std::vector<Vec3f> vert_positions;
	std::vector<Vec3f> vert_normals;

	std::vector<Vec2f> uv_pairs; // Must be a multiple of num_uv_mappings.
	
	std::vector<Triangle> triangles;
};


}


#endif // INDIGO_INDIGOMESH_H
