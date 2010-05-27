# Copyright (c) 2008-2010 Doug Hammond. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found at http://www.indigorenderer.com/opensource/licence.txt
#
#

class igmesh():
    '''
    Reads and writes .igmesh binary files.
    
    When writing, this class ASSUMES that the data held in
    it's member vars is exactly correct. No mesh data
    validation is performed other than
    - Check magic number
    - Check num_vert_normals is either ==0 or ==num_vert_positions
    
    Example usage:
    imr = igmesh()
    imr.load('mesh.igmesh')    # Load from file
    print(imr)                 # Prints out mesh info

    imr.save('re-mesh.igmesh') # Save to file
    print('Wrote %s bytes' % len(imr))
    '''
    
    # I/O control vars
    bytes_read = 0
    bytes_written = 0
    data_length = 0
    file_handle = None
    
    # .igmesh vars
    magic_number = None
    format_version = None
    num_uv_mappings = None
    num_used_materials = None
    used_materials = []
    uv_set_expositions = {}
    num_vert_positions = None
    vert_positions = []
    num_vert_normals = None
    vert_normals = []
    num_uv_pairs = None
    uv_pairs = []
    num_triangles = None
    triangles = []
    
    def __init__(self):
        from struct import calcsize, pack, unpack
        self.pack = pack
        self.unpack = unpack
        self.calcsize = calcsize
    
    def make_format(self, letter, count):
        return '<%i%s' % (count, letter)
    
    def get_chunk(self, length):
        c = self.file_handle.read(length)
        self.bytes_read += length
        return c
    
    def decode_header(self, headerbytes):
        self.magic_number, self.format_version, self.num_uv_mappings = self.unpack(self.make_format('I', 3), headerbytes)
    
    def decode_string(self):
        char8_length  = self.calcsize('c')
        length = self.decode_uint32()
        strg = self.unpack(self.make_format('c', char8_length*length), self.get_chunk(length))
        return ''.join([c.decode() for c in strg])
    
    def decode_uint32(self):
        uint32_length = self.calcsize('I')
        int32, = self.unpack(self.make_format('I', 1), self.get_chunk(uint32_length))
        return int32
    
    def decode_vec3f(self):
        float_length = self.calcsize('f')
        f = self.make_format('f', 3)
        return self.unpack(f, self.get_chunk(float_length*3))
    
    def decode_vec2f(self):
        float_length = self.calcsize('f')
        f = self.make_format('f', 2)
        return self.unpack(f, self.get_chunk(float_length*2))
    
    def decode_triangle(self):
        vertex_indices = [0,0,0]
        for i,v in enumerate(vertex_indices):
            vertex_indices[i] = self.decode_uint32()
            
        uv_indices = [0,0,0]
        for i,v in enumerate(uv_indices):
            uv_indices[i] = self.decode_uint32()
            
        mat_index = self.decode_uint32()
        
        return {
            'vertex_indices': vertex_indices,
            'uv_indices': uv_indices,
            'tri_mat_index': mat_index
        }
    
    def encode_uint32(self, val):
        f = self.make_format('I', 1)
        self.file_handle.write( self.pack(f, val) )
        self.bytes_written += self.calcsize('I')
        
    def encode_string(self, s):
        slen = len(s)
        f = self.make_format('I', 1)
        self.encode_uint32(slen)
        f = self.make_format('c', slen)
        self.file_handle.write( self.pack(f, *s) )
        self.bytes_written += slen * self.calcsize('c')
        
    def encode_vec3f(self, vec3f):
        f = self.make_format('f', 3)
        self.file_handle.write( self.pack(f, *vec3f) )
        self.bytes_written += 3 * self.calcsize('f')
        
    def encode_vec2f(self, vec2f):
        f = self.make_format('f', 2)
        self.file_handle.write( self.pack(f, *vec2f) )
        self.bytes_written += 2 * self.calcsize('f')
    
    def encode_triangle(self, tri):
        f1 = self.make_format('I', 1)
        f3 = self.make_format('I', 3)
        self.file_handle.write( self.pack(f3, *tri['vertex_indices'] ))
        self.bytes_written += 3 * self.calcsize('I')
        
        self.file_handle.write( self.pack(f3, *tri['uv_indices'] ))
        self.bytes_written += 3 * self.calcsize('I')
        
        self.file_handle.write( self.pack(f1, tri['tri_mat_index'] ))
        self.bytes_written += self.calcsize('I')
    
    def save(self, filename):
        self.bytes_written = 0
        
        self.magic_number =  5456751
        self.format_version = 1
        
        if self.num_vert_positions == 0:
            raise Exception('No vertex data to write')
        if self.num_vert_normals != 0 and self.num_vert_normals != self.num_vert_positions:
            raise Exception('Incorrect number of vertex normals')
        
        self.file_handle = open(filename, 'wb')
        
        # Header
        self.encode_uint32(self.magic_number)
        self.encode_uint32(self.format_version)
        self.encode_uint32(self.num_uv_mappings)
        
        # Materials
        self.encode_uint32(self.num_used_materials)
        for s in self.used_materials:
            self.encode_string(s)
            
        # UV Expositions
        self.encode_uint32(self.num_uv_set_expositions)
        for ind,name in self.uv_set_expositions.items():
            self.encode_string(name)
            self.encode_uint32(ind)
            
        # Vert Positions
        self.encode_uint32(self.num_vert_positions)
        for vp in self.vert_positions:
            self.encode_vec3f(vp)
            
        # Vert Normals
        self.encode_uint32(self.num_vert_normals)
        for vn in self.vert_normals:
            self.encode_vec3f(vn)
            
        # UV Pairs
        self.encode_uint32(self.num_uv_pairs)
        for uvp in self.uv_pairs:
            self.encode_vec2f(uvp)
            
        # Triangles
        self.encode_uint32(self.num_triangles)
        for tri in self.triangles:
            self.encode_triangle(tri)
        
        self.file_handle.close()
        
        # Update data_length so that len(self) is correct
        self.data_length = self.bytes_written
        
        return self.bytes_written
    
    def load(self, filename):
        self.bytes_read = 0
        
        # caller should handle exceptions
        from os.path import getsize
        self.data_length = getsize(filename)
        
        self.file_handle = open(filename, 'rb')
        
        # Header
        uint32_length = self.calcsize('I')
        self.decode_header(
            self.get_chunk(uint32_length*3)
        )
        
        if self.magic_number != 5456751:
            raise Exception('Invalid IGMESH File')
        
        # Materials
        self.num_used_materials = self.decode_uint32()
        self.used_materials = []
        for i in range(0,self.num_used_materials):
            strg = self.decode_string()
            self.used_materials.append(strg)
        
        # UV Expositions
        self.num_uv_set_expositions = self.decode_uint32()
        self.uv_set_expositions = {}
        for i in range(0, self.num_uv_set_expositions):
            name = self.decode_string()
            ind = self.decode_uint32()
            self.uv_set_expositions[ind] = name
            
        # Vert Positions
        self.num_vert_positions = self.decode_uint32()
        self.vert_positions = []
        for i in range(0, self.num_vert_positions):
            self.vert_positions.append(self.decode_vec3f())
            
        # Vert Normals
        self.num_vert_normals = self.decode_uint32()
        self.vert_normals = []
        for i in range(0, self.num_vert_normals):
            self.vert_normals.append(self.decode_vec3f())
            
        # UV Pairs
        self.num_uv_pairs = self.decode_uint32()
        self.uv_pairs = []
        for i in range(0, self.num_uv_pairs):
            self.uv_pairs.append(self.decode_vec2f())
            
        # Triangles
        self.num_triangles = self.decode_uint32()
        self.triangles = []
        for i in range(0, self.num_triangles):
            self.triangles.append(self.decode_triangle())
            
        self.file_handle.close()
            
        if not self.data_length == self.bytes_read:
            raise Exception('IGMESH data not read completely')
    
    def __len__(self):
        return self.data_length        
    
    def __str__(self):
        return '''<igmesh
        \tMagic Number:           %s
        \tFormat Version:         %s
        \tNum UV Mappings:        %s
        \tNum Used Materials:     %s
        \tUsed Materials:         %s
        \tNum UV Set Expositions: %s
        \tUV Set Expositions:     %s
        \tNum vert positions:     %s
        \tVert positions:         <list length %s>
        \tNum Vert Normals:       %s
        \tVert Normals:           <list length %s>
        \tNum UV Pairs:           %s
        \tUV Pairs:               <list length %s>
        \tNum Triangles:          %s
        \tTriangles:              <list length %s>
        \tData size:              %s bytes
>''' % (
                self.magic_number,
                self.format_version,
                self.num_uv_mappings,
                self.num_used_materials,
                self.used_materials,
                self.num_uv_set_expositions,
                self.uv_set_expositions,
                self.num_vert_positions,
                len(self.vert_positions),
                self.num_vert_normals,
                len(self.vert_normals),
                self.num_uv_pairs,
                len(self.uv_pairs),
                self.num_triangles,
                len(self.triangles),
                len(self)
            )