# Indigo Scene Format Technical Reference

For Indigo Renderer version 2.0.x 

Copyright (c) Glare Technologies 2004-2010.

Contributors:

 * Nicholas Chapman
 * Ben Nolan
 * Thomas Ludwig
 * Yves Collé


Last updated 27th May 2010

## Overview of this document

The Indigo scene format is a freely usable scene format for describing physically accurate 3 dimensional scenes. It has been developed in conjunction with [Indigo Renderer](http://www.indigorenderer.com/), a physically based, unbiased raytracer. This format has been available for public use for several years, but in 2010 we decided to officially relicence the format and it's supporting documentation under opensource licences - so that other 3D packages can use the Indigo format as they see fit.

Please not that the Indigo application is not opensourced, and software that uses the Indigo Scene Format is not required to be opensourced either. Commercial, free and opensource software may all use Indigo equally.

## Introduction to the .IGS format

Indigo scene files are stored in an XML format. The filename extension 
is .igs, for 'Indigo Scene'. 

Root element should be called 'scene'. 

renderer_settings 

This element provides a means of overriding various settings 
from inifile.xml. This element is optional, and so are each of 
its children. Any setting defined here overrides the respective 
setting from inifile.xml. 

**element status: **optional 

### width

Sets the width (horizontal resolution) of the output image. 

**type**: integer 

**restrictions**: must be > 0 

**units**: pixels 

**default value**: 600 

### height

Sets the height (vertical resolution) of the output image. 

**type**: integer 

**restrictions**: must be > 0 

**units**: pixels 

**default value**: 450 

### bih_tri_threshold

If the number of triangles in a single mesh exceeds this threshold, 
then a BIH will be used for intersection accleration for that 
mesh, otherwise a Kd-tree is used. 

**type**: integer 

**restrictions**: must be > 0 

**units**: number of triangles 

**default value**: 1100000 

### metropolis

Enables or disables Metropolis-Hastings sampling 

{text:soft-page-break} **type**: boolean 

**default value**: true 

### large_mutation_prob

Probability of selecting a large mutation type. Only used if 
metropolis is true. 

**type**: scalar real 

**restrictions**: must in range [0, 1] 

**units**: dimensionless 

**default value**: 0.4 

### max_change

Radius of the perturbation mutation distribution. 

**type**: scalar real 

**restrictions**: must in range [0, 1] 

**units**: dimensionless 

**default value**: 0.01 

### max_depth

Maximum ray bounce depth. 

**type**: integer 

**restrictions**: must be > 0 

**units**: number of bounces 

**default value**: 10000 

### max_num_consec_rejections

Maximum number of consecutive rejection of tentative new samples 
when Metropolis-Hastings transport is used. Note that any non-infinite 
number technically causes biased sampling. 

**type**: integer 

**restrictions**: must be > 0 

**units**: number of rejections 

{text:soft-page-break} **default value**: 1000 

### logging

If true, a log of the console output is written to log.txt 

**type**: boolean 

**default value**: true 

### bidirectional

If true, bidirectional path tracing is used to construct paths. 
Otherwise, backwards path tracing is used. 

**type**: boolean 

**default value**: true 

### save_untonemapped_exr

If true, an untonemapped EXR image is saved in the renders directory. 

**type**: boolean 

**default value**: false 

### save_tonemapped_exr

If true, a tonemapped EXR image is saved in the renders directory. 

**type**: boolean 

**default value**: false 

### save_igi

If true, an untonemapped Indigo Image (.igi) file is saved in 
the renders directory. 

**type**: boolean 

**default value**: false 

### image_save_period

The rendered image(s) will be saved to the renders directory 
every image\_save\_period seconds. 

**type**: scalar real 

{text:soft-page-break} **restrictions**: must be > 0 

**units**: seconds 

**default value**: 10 

### halt_time

If positive, indigo will halt after halt\_time seconds. 

**type**: scalar real 

**restrictions**: 

**units**: seconds 

**default value**: -1 

### halt_samples_per_pixel

If positive, indigo will halt after halt\_samples\_per\_pixel 
samples per pixel have been reached. 

**type**: scalar real 

**restrictions**: 

**units**: samples / pixel 

**default value**: -1 

### {text:bookmark-start} h {text:bookmark-end} ybrid

If true, direct illumination is sampled with QMC sampling, and 
indirect illumination with Metropolis-Hastings sampling. 

**type**: boolean 

**default value**: false 

### frame_upload_period

Period between uploads of the image buffer from slave to master 
when rendering in network mode. 

**type**: scalar real 

**restrictions**: must be > 0 

**units**: seconds 

{text:soft-page-break} **default value**: 40 

### auto_choose_num_threads

If true, the number of render threads used is set based on the number 
of logical cores detected. 

**type**: boolean 

**default value**: true 

### num_threads

Number of render threads used. This setting is only used if auto\_choose\_num\_threads 
is false. 

**type**: integer 

**restrictions**: must be > 0 

**units**: number of threads 

**default value**: 1 

### super_sample_factor

If this factor is greater than 1, then the image is rendered at 
a higher resolution internally, then downsampled using the 
downsize filter before the render is saved to disk. This can help 
to reduce aliasing around high contrast edges. 

Note that higher factors require more memory (RAM). 

**type**: integer 

**restrictions**: must be > 0 

**units**: dimensionless 

**default value**: 2 

### display_period

The internal HDR buffer is tonemapped and displayed on screen 
every display\_period seconds. 

**type**: scalar real 

**restrictions**: must be > 0 

**units**: seconds 

**default value**: 10 

### {text:soft-page-break} ray_origin_nudge_distance

Ray origins are offset by this distance after intersection, 
in order to avoid false self-intersections. 

**type**: scalar real 

**restrictions**: must be >= 0 

**units**: meters 

**default value**: 1.0e-4 

### watermark

If true, an 'Indigo Renderer' logo is drawn on the bottom right 
hand corner of the output render. 

**type**: boolean 

**default value**: false 

### info_overlay

If true, a line of text is drawn on the bottom of each render, containing 
some statistics about the current render process. 

**type**: boolean 

**default value**: false 

### cache_trees

If true, kd-trees are cached to disk after construction, in the 
tree_cache directory. 

**type**: boolean 

**default value**: true 

### aperture_diffraction

If true, diffraction of light passing through the camera aperture 
is simulated. 

**type**: boolean 

**default value**: true 

### post_process_diffraction

If true, aperture_diffraction is simulated using a filter applied 
to the image buffer, instead of perturbation of rays. This technique 
is generally faster and less noisy, but slightly less accurate. 

{text:soft-page-break} **type**: boolean 

**default value**: true 

### render_region

If this element is present, only a certain region of the usual 
image is rendered. 

Only pixels (x, y) such that x1 <= x < x2 and y1 <= y < y2 are rendered. 

render_region::x1 

X Coordinate of top left pixel of rendered region. 

**type**: integer 

**restrictions**: must be >= 0 

**units**: pixels 

render_region::y1 

Y Coordinate of top left pixel of rendered region. 

**type**: integer 

**restrictions**: must be >= 0 

**units**: pixels 

render_region::x2 

X Coordinate of pixel immediately to the right of rendered region. 

**type**: integer 

**restrictions**: x1 < x2 <= width 

**units**: pixels 

render_region::y2 

Y Coordinate of pixel immediately below rendered region. 

**type**: integer 

**restrictions**: y1 < y2 <= height 

**units**: pixels 

{text:soft-page-break} render_foreground_alpha 

If this is true, the output image is just a greyscale image, where 
the foreground is white, and the background (physical sky, env 
map, constant background, void background etc..) is black. 

**type**: boolean 

**default value: **false 

splat_filter 

Controls the filter used for splatting contributions to the 
image buffer. 

Can be one of box, gaussian, or mn\_cubic. 

splat_filter::box 

Box filter. Causes bad aliasing, don't use :) 

splat_filter::gaussian 

Gaussian filter with standard deviation of 0.35 pixels. 

splat_filter::mn_cubic 

Mitchell-Netravali cubic filter. Good all-round filter with 
little aliasing. 

Please refer to the paper 'Reconstruction Filters in Computer 
Graphics' by Mitchell and Netravali, 1988, for more information. 

splat_filter::mn_cubic::blur 

The 'B' parameter from the paper. Higher blur values cause more 
blurring of the image 

**type**: scalar real 

**restrictions**: will give best results in range [0, 1] 

**units**: dimensionless 

**default value**: 0.6 

splat_filter::mn_cubic::ring 

The 'C' parameter from the paper. Higher ring values cause more 
'ringing'. (alternating bands of black and white around high 
contrast edges). 

Note that Mitchell and Netravali recommend choosing B and C such 
that 2C + B = 1. 

{text:soft-page-break} **type**: scalar real 

**restrictions**: will give best results in range [0, 1] 

**units**: dimensionless 

**default value**: 0.2 

downsize_filter 

Controls the filter used for downsizing super-sampled images. 

Only used when super_sample_factor is greater than one. 

Takes exactly the same parameters as splat\\_filter. 

Example XML for renderer_settings: 

    <renderer_settings>
        <metropolis>true</metropolis>
        <bidirectional>true</bidirectional>
    
        <width>800</width>
        <height>600</height>
    
        <downsize_filter>
            <mn_cubic>
                <ring>0.2</ring>
                <blur>0.6</blur>
            </mn_cubic>
        </downsize_filter>
        <splat_filter>
            <gaussian/>
        </splat_filter>
    
        <super_sample_factor>2</super_sample_factor>
    
        <aperture_diffraction>true</aperture_diffraction>
        <post_process_diffraction>true</post_process_diffraction>
    </renderer_settings>

background
----------

Illuminates scene with a uniform environment light. 

element status: optional 

Must have exactly one 'spectrum' child element. 

example xml: 

    <background>
            <spectrum>
                    <blackbody>
                            <temperature>3500</temperature>
                            <gain>1.0</gain>
                    </blackbody>
            </spectrum>
    </background>

skylight
--------

<img src='Pictures/1000000000000320000002585C50A929.jpg' 
/>Illuminates scene with sunlight and scattered skylight. 

element status: optional 

### sundir

The sundir element defines the 3-vector direction towards the 
sun. the Z axis is up, e.g. (0,0,1) places the sun directly overhead. 
Need not be normalised 

**type**: real 3-vector 

**restrictions**: z component must be > 0 

**units**: dimensionless 

### turbidity

The turbidity defines the haziness/clearness of the sky. Lower 
turbidity means a clearer sky. Should be set to something between 
2 and ~5. 

**type**: scalar real 

**restrictions**: > 0 

**units**: dimensionless 

### extra_atmospheric

If extra_atmospheric is true, then the skylight is computed 
as if it was outside the atmosphere. 

This means that the sun spectrum is not attenuated by atmospheric 
scattering, and the sky will be black, since {text:soft-page-break} 
there is no atmospheric scattering. 

**Element status**: optional 

**type**: boolean 

**default**:false 

xml example: 

    <skylight>
            <sundir>0 0.6 1</sundir>
            <turbidity>2</turbidity>

</skylight> 

env_map
-------

<img src='Pictures/1000000000000280000001E0C9A64A64.jpg' 
/>element status: optional 

Illuminates scene with a HDR environment map. 

Currently Indigo can load two types of environment maps. 

The first type is .exr maps in lat-long format: 

### env_map :: lat_long

### env_map :: lat_long :: path

The path to the .exr file. 

**type**: string 

**restrictions**: must be a valid path 

**units**: 

### env_map :: lat_long :: gain

The map is scaled by this factor when it is loaded. 

**type**: scalar real 

**restrictions**: > 0 

{text:soft-page-break} **units**: dimensionless 

The second type of Env map supported by Indigo is .float maps in 
spherical format. .float is a simple format exported by the HDR 
Shop program, with 3 32bit floats per pixel, one per colour channel, 
and no other information in the file. 

### env_map :: spherical

### env_map :: spherical :: path

The path to the .exr file. 

**type**: string 

**restrictions**: must be a valid path 

**units**: 

### env_map :: spherical :: width

The width of the map. Must be equal to the height 

**type**: scalar integer 

**restrictions**: > 0 

**units**: pixels 

### env_map :: spherical :: gain

The map is scaled by this factor when it is loaded. 

**type**: scalar real 

**restrictions**: > 0 

**units**: dimensionless 

Example XML: 

    <env_map>
            <spherical>
                <path>probes/kitchen_probe.float</path>
                <width>640</width>
                <gain>0.9</gain>
            </spherical>
            
     {text:soft-page-break}         <!--latlong>
                <path>probes/skylight-day.exr</path>
                <gain>1.0</gain>
            </latlong-->
    </env_map>
    

Tonemapping
-----------

The tonemapping element should have one child element, either 
'linear', 'reinhard', or 'camera'. 

element status: required 

### tonemapping :: linear

### tonemapping :: linear :: scale

A constant by which the pixel values are multiplied. 

**type**: scalar real 

**restrictions**: >= 0 

**units**: dimensionless 

### tonemapping :: reinhard

### tonemapping :: reinhard :: pre_scale

**type**: scalar real 

**restrictions**: >= 0 

**units**: dimensionless 

### tonemapping :: reinhard :: post_scale

This scaling factor is applied after the rest of the tone mapping 
stages. By default, the pixel with max luminance is mapped to 
white, so setting this scale to > 1 will result in pixels with less 
luminance being mapped to white. example: 

**type**: scalar real 

**restrictions**: >= 0 

**units**: dimensionless 

### {text:soft-page-break} **tonemapping :: reinhard :: burn**

Determines the luminance at which clipping occurs. 

A smaller value means more severe burn, no burn will occur in the 
limit as the value goes to infinity. 

element status: optional 

**type**: scalar real 

**restrictions**: > 1 

**units**: dimensionless 

**default value**: 10 

### tonemapping :: camera

Camera tone mapping is an attempt to model the image generation 
process of a digital camera, and shares some parameters with 
a real camera. 

The response function uses data from 

http://www1.cs.columbia.edu/CAVE/software/softlib/dorf.php 

, as such many cameras should be able to be modelled. 

### tonemapping :: camera :: response\\_function\\_path

**Path to response function data file, e.g. 'data/camera\\_response\\_functions/dscs315.txt'** 

**Path can be absolute or relative; if relative, it is taken relative 
to the Indigo executable base path.** 

**type**: string 

**restrictions**: 

**units**: 

### tonemapping :: camera :: ev\\_adjust

**ev\\_adjust is exposure-value adjustment; increasing this 
value by 1 will effectively double the 'sensor output'.** 

**type**: real scalar 

**restrictions**: 

**units**: dimensionless 

### {text:soft-page-break} tonemapping :: camera :: film\\_iso

**film speed (film ISO) has much the same effect as ev\\_adjust, 
except it's a linear factor. Doubling the film ISO will double 
the 'sensor output'.** 

**type**: real scalar 

**restrictions**: must be > 0 

**units**: dimensionless 

xml example: 

    <tonemapping>
            <reinhard>
                    <pre_scale>1.0</pre_scale>
                    <post_scale>1.0</post_scale>
            </reinhard>

</tonemapping> 

Camera
------

**element status: **required 

### pos

Defines the position of the camera. 

**type**: real 3-vector 

**restrictions**: 

**units**: meters 

### up

Defines the up vector of the camera. This and the forwards vector 
uniquely determine the right vector. Need not be normalised. 

type: real 3-vector 

**restrictions**: 

**units**: dimensionless 

### forwards

Defines the forwards vector of the camera, i.e. which direction 
it is facing. Need not be normalised. 

type: real 3-vector 

**restrictions**: 

**units**: dimensionless 

### aperture_radius

Defines the radius of the camera aperture. Larger radius means 
more depth of field. 

If a non-circular aperture is used, then aperture_radius defines 
the half-width of the rectangle in which the aperture shape is 
defined. 

**type**: scalar real 

**restrictions**: Must be greater than zero. 

**units**: meters 

### {text:soft-page-break} focus_distance

Distance from the camera, along the camera forwards direction, 
to the focal plane. Objects lying on the focal plane will be in 
focus. Value not used if autofocus is set. 

**type**: scalar real 

**restrictions**: Must be greater than zero. 

**units**: meters 

### aspect_ratio

Influences the directions in which rays are traced. Should be 
set to the image width divided by the image height. 

**type**: scalar real 

**restrictions**: Must be greater than zero. 

**units**: dimensionless 

### sensor_width

Width of the sensor element of the camera. A reasonable default 
is 0.036. (36mm) 

Determines the angle of view (FOV), together with the lens_sensor_dist. 

**type**: scalar real 

**restrictions**: Must be greater than zero. 

**units**: meters 

### lens_sensor_dist

Distance from the camera sensor to the camera lens. A reasonable 
default is 0.02. (20mm) 

**type**: scalar real 

**restrictions**: Must be greater than zero. 

**units**: meters 

### white_balance

Sets the white balance of the camera. 

Possible values are D50, D55, D65 etc.. {text:line-break} all 
the illuminants from [**http://en.wikipedia.org/wiki/White\\_point**](http://en.wikipedia.org/wiki/White_point) 
are supported. 

{text:soft-page-break} What's this for? {text:line-break} 
Well lets say you're rendering a room illuminated by a 5000K blackbody 
emitter. {text:line-break} In real life, your eyes would adjust 
to the lighting conditions, and you would perceive the light 
as white. {text:line-break} The same would occur in a room lit 
by a 6500K blackbody emitter. {text:line-break} A whitebalance 
setting allows the camera to adjust in the same way that the eyes 
do. {text:line-break} So if you set the white balance to D50 and 
render the room with a 5000K emitter, the light should appear 
white. {text:line-break} If you set the white balance to D65 
it will come out kinda orange. {text:line-break} The D65 white 
point is designed for outdoors and is a good general setting to 
use if you're not sure what to use. 

**type**: string 

**restrictions**: Must be one of 'D65', 'D50', 'E' etc.. 

### exposure_duration

How long the exposure will be. The longer the exposure duration, 
the greater the light energy registered by the sensor. 

**type**: scalar real 

**restrictions**: Must be greater than zero. 

**units**: seconds 

### autofocus

If this (empty) element is present, a ray will be traced from the 
camera position in the camera forwards direction. The camera 
focus distance will then be set to the distance the ray travels 
before striking an object, or to infinity if no object is hit. 

Element status: optional 

### obstacle_map

If this element is present, then an obstacle map texture is used 
when calculating the diffraction though the camera aperture. 

An obstacle map will only have an effect if aperture_diffraction 
is enabled. 

**Path must be relative to the scene working directory.** 

**Element status**: optional 

**type**: string 

### aperture_shape

If the aperture_shape element is not present, then a default 
circular aperture shape is used. 

Note that a preview of the final aperture shape will be saved in 
the working directory as aperture\_preview.png. 

**Element status**: optional 

### aperture\\_shape::circular

Makes the camera use a circular shaped aperture. 

### aperture\\_shape::image

Allows the aperture shape to be loaded from an image file. 

### aperture\\_shape::image::path

**The path to the aperture image file.** 

**The image must be of PNG format.** 

**The image is interpreted as a greyscale image.** 

**The image must be square, and have power-of-two dimensions 
of at least 512 x 512.** 

**White portions of the image are interpreted as transparent, 
and black parts of the image are interpreted as stopping light.** 

**The white part of the aperture image should be as large as possible 
(i.e. It should just touch the edges of the square image), to allow 
for efficient sampling.** 

**Path must be relative to the scene working directory.** 

**type**: string 

### aperture\\_shape::generated

Allows the aperture shape to be defined using a few parameters. 
See the attached digram for more information. 

### aperture\\_shape::generated::num\\_blades

Number of diaphragm blades. 

**type**: integer 

**restrictions**: Must be >= 3 

{text:soft-page-break} **units**: dimensionless 

### aperture\\_shape::generated::start\\_angle

Initial angle of first diaphragm blade. 

**type**: scalar real 

**restrictions**: 

**units**: radians 

### aperture\\_shape::generated::blade\\_offset

Distance from center of aperture shape to edge of diaphragm. 

**type**: scalar real 

**restrictions**: must be > 0 

**units**: fraction of aperture shape width 

### aperture\\_shape::generated::blade\\_curvature\\_radius

Distance from edge of diaphragm to effective center of diaphragm 
curvature circle. 

**type**: scalar real 

**restrictions**: must be > 0 

**units**: fraction of aperture shape width 

### Camera element example XML:

    <camera>
            <pos>0 -2 1</pos>
            <up>0 0 1</up>
            <forwards>0 1 0</forwards>
            <aperture_radius>0.001</aperture_radius>
            <focus_distance>3.0</focus_distance>
            <aspect_ratio>1.33</aspect_ratio>
            <sensor_width>0.036</sensor_width>
            <lens_sensor_dist>0.02</lens_sensor_dist>
            <white_balance>E</white_balance>
    
        <autofocus/>

</camera> 

{text:soft-page-break} 

Materials
---------

### Texture

The final, used value for each component is calculated like so: 

f(x) = a*g(x)2 + b*g(x) + c 

and 

g(x) = xexponent 

Where x is the colour component from the map (e.g. The greyscale 
value or one of the R, G, B), normalised to [0, 1], 

f(x) is the final used value, and a, b, c, and exponent are as described 
below. 

In the case where are scalar value is required from a RGB map, for 
example when using a bump map, 

the final value is calculated as (f(r) + f(g) + f(b)) / 3 

Supported texture formats: 

JPEG (.jpg, .jpeg): greyscale, RGB supported. 

PNG (.png): greyscale (8 or 16 bits per pixel) , RGB (24 or 48 bits 
per pixel) supported. Note that 16 bits per channel data will 
be internally converted to 8 bits per channel data. 

Truevision TGA (.tga): greyscale (8 bits per pixel) or RGB (24 
bits per pixel) supported. RLE compression is not supported. 

**Windows Bitmap** (.bmp): greyscale (8 bits per pixel) or RGB 
(24 bits per pixel) supported. RLE compression is not supported. 

**Open EXR** (.exr) 

**TIFF (.tif / .tiff): **greyscale, RGB, RGBA supported. 

### texture::uv_set

Name of the set of uv coordinates used for texture lookup. 

**type**: string 

**restrictions**: must be a uv set that has been exported by a 
mesh, if the material is used on that mesh. 

**units**: 

### {text:soft-page-break} texture::path

**Path to the texture on disk. Path must be absolute or relative 
to the scene working directory.** 

**type**: string 

### texture::exponent

Used for converting texture RGB values to display values. A typical 
value is thus 2.2. 

**type**: scalar real 

**restrictions**: must be > 0 

**units**: dimensionless 

### texture::a

'a' coefficient for quadratic texture function. 

Element status: optional 

### texture::b

'b' coefficient for quadratic texture function. 

Element status: optional 

### texture::c

'c' coefficient for quadratic texture function. 

Element status: optional 

### texture::tex_coord_generation

Determines how texture coordinates are generated. 

### texture::tex_coord_generation::uv

Texture coordinates will be generated by multiplying the geometry 
uv coordinates by an affine transformation. 

### texture::tex_coord_generation::uv::matrix

A 2x2 matrix that is multiplied with the geometry uv coordinates. 

### {text:soft-page-break} texture::tex_coord_generation::uv::translation

A 2-vector that specifiies a translation. 

example xml: 

    <texture>
            <uv_set>albedo</uv_set>
            <path>__55_Chevy_by_marpo3.jpg</path>
            <exponent>2.2</exponent>
            <tex_coord_generation>
              <uv>
                <matrix>1 0 0 1</matrix>
                <translation>0.5 0.5</translation>
              </uv>
            </tex_coord_generation>
    texture>

material
--------

Defines a material. 

A material element must have one child element called 'name', 
and another element which can be either 'specular', 'phong', 
or 'diffuse' etc.. 

### material :: name

The name of the material 

**type**: string 

**restrictions**: 

**units**: 

diffuse
-------

<img src='Pictures/10000000000001F4000001F408270D32.png' 
/> 

Diffuse is a Lambertian diffuse material. 

### {text:reference-mark}  {text:reference-mark} albedo

Sets the reflectance (albedo) 

Values will be clamped to the range [0, 1]. 

Type: wavelength-dependent material parameter. 

**units**: dimensionless 

bump 

The bump map is used to perturb the shading normal of the surface. 

**element\_status**: optional 

{text:soft-page-break} **type**: displacement material 
parameter. 

**units**: meters 

displacement 

The displacement distance in meters that mesh vertices are displaced 
along the shading normal. 

**element\_status**: optional 

**type**: displacement material parameter. 

**units**: meters 

base_emission 

The spectral radiance emitted from this material surface. 

Values will be clamped to [0, infinity) 

**element\_status**: optional 

**type**: wavelength-dependent material parameter. 

**units**: W m-3 sr-1 

emission 

Modulates the base_emission value: the final emitted spectral 
radiance is calculated as the product of base_emission and emission. 

Values will be clamped to [0, infinity) 

**element\_status**: optional 

**type**: wavelength-dependent material parameter. 

**Units**: dimensionless 

layer 

Defines the index of the layer that light emitted from this material 
will be drawn to. The index is zero-based. 

**element\_status**: optional 

**type**: integer 

**default**: 0 

{text:soft-page-break} 

example xml: 

    <material>
        <name>mat1</name>
        <diffuse>
            <texture>
                <uv_set>albedo</uv_set>
                <path>indigo_logo.png</path>
                <exponent>2.2</exponent>
            </texture>
    
    
            <base_emission>
                <constant>
                    <rgb>
                        <rgb>
                            2000000000 2000000000 2000000000
                        </rgb>
                        <gamma>1</gamma>
                    </rgb>
                </constant>
            </base_emission>
        </diffuse>
    </material>

specular
--------

<img src='Pictures/10000000000001F4000001F40CBBC7E5.png' 
/> 

Specular is a material that can be both a perfect specular reflector 
and a perfect specular transmitter. 

### internal_medium_name

Should be the name of a medium already defined in the scene file. 

type: {text:reference-ref} {text:reference-ref} string 

unit: 

restrictions: 

### transparent

true or false. If true, light can be transmitted, if not, only 
reflected light is simulated. 

type: boolean 

{text:soft-page-break} bump 

See diffuse::bump 

displacement 

See diffuse::displacement 

base_emission 

See diffuse::base_emission 

emission 

See diffuse::emission 

layer 

See diffuse::layer 

xml example: 

    <specular>      
            <transparent>true</transparent>         
            <internal_medium_name>glass</internal_medium_name>

</specular> 

phong
-----

<img src='Pictures/10000000000001F4000001F4C7F9A75E.png' 
/> 

Phong is a physically based glossy reflection model using a Phong 
lobe. It has a Lambertian diffuse substrate. 

### diffuse_albedo

The reflectance of the diffuse substrate. 

Values will be clamped to the range [0, 1]. 

**type: ****wavelength-dependent material parameter** 

**units**: dimensionless 

### ior

Index of refraction of the dielectric coating or substance making 
up the material. 

{text:soft-page-break} **type**: real scalar 

**units**: dimensionless 

**restrictions: ****>= 1** 

### exponent

Sets the exponent of the Phong lobe controlling specular reflection. 
Higher exponent means more 'perfect' reflection, lower exponent 
leads to more glossy+diffuse highlights. Can range from ~1 to 
up to 10000 or more. 

**type: ****wavelength-independent material parameter** 

units: dimensionless 

**restrictions: **Must be greater than zero. 

### nk_data

<img src='Pictures/100000000000032000000258F134BD83.jpg' 
/>The nk_data element specifies that the phong material should 
use measured complex IOR data to compute the reflection at various 
angles. 

If nk_data is specified, then the diffuse and specular elements 
are not taken into account. 

The value of the nk_data element should be a path to a .nk file, 
e.g. 'nkdata/au.nk' 

**element status: **optional 

**type**: string 

**restrictions: **Must be a valid path to a .nk file. Path should 
be a relative path from Indigo root directory. 

### {text:soft-page-break} specular_reflectivity

The specular reflectivity at normal incidence. 

If this element is present, then the specular reflectivity at 
various angles is based on these values. 

If this element is present, then the diffuse albedo of the material 
is set to zero, therefore, if this element is present, only metals 
can be simulated. 

If this element is present, then the ior and diffuse\_albedo 
elements are ignored. 

Values will be clamped to lie in the range [0, 1] 

**type: ****wavelength-dependent material parameter** 

**units**: dimensionless 

bump 

See diffuse::bump 

displacement 

See diffuse::displacement 

base_emission 

See diffuse::base_emission 

emission 

See diffuse::emission 

layer 

See diffuse::layer 

xml example: 

    <material>
        <name>phong1</name>
        <phong>
            <ior>1.5</ior>
            <exponent>
                <constant>
                    10.0
                </constant>
            </exponent>
            <diffuse_albedo>
                <constant>
                    <uniform>
                        <value>0.3</value>
                    </uniform>
     {text:soft-page-break}             </constant>
            </diffuse_albedo>
        </phong>       
    </material>

or 

    <material>
        <name>aluminium</name>        
        <phong>
            <nk_data>nkdata/al.nk</nk_data>
            <exponent>
                <constant>1000</constant>
            </exponent>
        </phong>
    </material>
    

or 

<material> 

<name>phong2</name> 

<phong> 

<exponent> 

<constant>100</constant> 

</exponent> 

<specular_reflectivity> 

<constant> 

<rgb> 

<rgb>0.8 0.2 0.2</rgb> 

<gamma>1</gamma> 

</rgb> 

</constant> 

</specular_reflectivity> 

</phong> 

</material> {text:line-break} 

glossy_transparent
------------------

<img src='Pictures/10000000000001F4000001F4A433AC6D.png' 
/>The glossy transparent is a material that simulates a rough 
surface of a transparent dielectric medium. It's good for simulating 
stuff like frosted glass, human skin etc... 

### internal_medium_name

Should be the name of a medium already defined in the scene file. 

**type**: string 

### exponent

See phong::exponent 

bump 

See diffuse::bump 

{text:soft-page-break} displacement 

See diffuse::displacement 

base_emission 

See diffuse::base_emission 

emission 

See diffuse::emission 

layer 

See diffuse::layer 

XML example: 

    <material>
        <name>frosty_glass</name>
    
        <glossy_transparent>
            <internal_medium_name>glass</internal_medium_name>
            <exponent>
                <constant>1000</constant>
            </exponent>
        </glossy_transparent>
    </material>

diffuse_transmitter
-------------------

<img src='Pictures/10000000000001F4000001F4EA127B6E.png' 
/>Note: Image shows a blend of diffuse transmitter and Phong 
materials 

This material is a very simple BSDF that basically scatters incoming 
light into the opposite hemisphere, with a cosine-weighted 
distrubution. {text:line-break} Although it doesn't really 
have any exact physical basis, it could be thought of as the limit 
of many sub-surface scatters inside a thin, highly scattering 
material. As such it should be useful for simulating such materials 
as curtains, lampshades etc.. {text:line-break} It's meant 
to be used on single-layer geometry, and it does not have an associated 
internal medium (it's not an interface material). {text:line-break} 
It will probably be a good idea to blend this material with a diffuse 
or phong material, so that some backscattered light is visible, 
not just transmitted light. 

### albedo

Sets the transmission fraction (albedo) 

Values will be clamped to the range [0, 1.0]. 

Type: wavelength-depenedent material parameter 

**units**: dimensionless 

{text:soft-page-break} displacement 

See diffuse::displacement 

base_emission 

See diffuse::base_emission 

emission 

See diffuse::emission 

layer 

See diffuse::layer 

xml example: 

    <material>
        <name>diff_tran</name>
            
        <diffuse_transmitter>
            <texture>
                <uv_set>albedo</uv_set>
                <path>ColorChecker_sRGB_from_Ref.jpg</path>
                <exponent>2.2</exponent>
            </texture>
                
            <albedo>
                <texture>
                    <texture_index>0</texture_index>
                </texture>
            </albedo>
        </diffuse_transmitter>
    </material>

blend
-----

<img src='Pictures/10000000000001F4000001F4A26FAFDC.png' 
/>The blend material allows two materials to be blended together, 
with the weighting factor a given constant, or controlled by 
an image map. 

More than two materials can be blended, by using a hierarchical 
arrangement of blend materials. 

There is one restriction that applies to what materials can be 
blended together (in the same blend tree composed of one or more 
blend materials) – At most one constituent material can be a BSDF 
containing a delta distribution. Materials with delta distributions 
are the specular and null_material material types. 

### blend

Controls the fraction of each constituent material used. 

Will be clamped to [0, 1] 

**type**: wavelength-independent material parameter 

**units**: dimensionless 

### {text:soft-page-break} step_blend

If step_blend is true, then the blend parameter will have the 
following step function applied to it: 

f(x) = 1 if x >= 0.5, else 0 

Enabling step blend is recommended when using a texture as a 'clip 
mask', in order to reduce noise. 

**type**: boolean 

**default: ****false** 

### a_name

Name of constituent material a. 

**type**: string 

b_name 

Name of constituent material b. 

**type**: string 

xml example: 

    <material>
        <name>mata</name>
        <phong>
            <ior>3</ior>
            <diffuse>1 0 0</diffuse>
            <exponent>10000</exponent>
            
            <bump_map>
                <uv_set>bump</uv_set>
                <path>indigo.jpg</path>
                <b>0.003</b>
                <exponent>1.0</exponent>
            </bump_map>
        </phong>
    </material>
    
    <material>
        <name>matb</name>
        <diffuse>
            <colour>0 1 0</colour>
            
            <bump_map>
                <uv_set>bump</uv_set>
                <path>spherebump.jpg</path>
                <b>0.1</b>
                <exponent>1.0</exponent>
            </bump_map>
        </diffuse>
    </material>
    
    <material>
        <name>blendmat</name>
            
        <blend>
            <a_name>a</a_name>
            <b_name>b</b_name>
            <texture>
                <uv_set>albedo</uv_set>
                <path>checker.jpg</path>
                <exponent>1.0</exponent>
            </texture>
                <blend>
            <texture>
                    <texture_index>0</texture_index>
                </texture>
            </blend>
        </blend>
    </material>

{text:soft-page-break} 

null_material
-------------

The null material is a very simple material that doesn't scatter 
light at all. It's effectively invisible. 

The null material has no parameters. 

Xml example: 

    <material>
        <name>b</name>
        <null_material/>
    </material>
    

oren_nayar
----------

<img src='Pictures/10000000000001F4000001F4F1D2B081.png' 
/>The Oren-Nayar material models very rough surfaces that have 
no specular reflection. 

It's appropriate for materials like clay, sprayed concrete, 
porous rock, Moon surface, etc.. 

<img src='Pictures/100000000000050000000296C1F1D0F6.png' 
/>Dependence of the Oren-Nayar material on the sigma parameter. 
Render by Zom-B, model from The Stanford 3D Scanning Repository 

### {text:soft-page-break} sigma

Controls the roughness of the material. A higher sigma gives 
a rougher material with more backscattering. 

Standard deviation of the microfacet groove slope angles. 

Values will be clamped to [0, infinity) 

**type**: wavelength-independent material parameter 

**units**: radians 

### albedo

See diffuse::albedo 

bump 

See diffuse::bump 

displacement 

See diffuse::displacement 

base_emission 

See diffuse::base_emission 

emission 

See diffuse::emission 

{text:soft-page-break} layer 

See diffuse::layer 

Xml example: 

    <material>
        <name>3</name>
        <oren_nayar>
            <albedo>
                <constant>
                    <uniform>
                        <value>0.7</value>
                    </uniform>
                </constant>
            </albedo>
            <sigma>
                <constant>0.2</constant>
            </sigma>
        </oren_nayar>
    </material>

Medium
------

### medium

Defines a new medium. A medium has a type (much like material have 
types). 

Media types include basic, epidermis, and dermis. 

### name

**Name of the medium. Used when specifying the internal\\_medium\\_name 
in specular etc.. materials.** 

**type: ****string** 

**unit**: 

**restrictions:** 

### precedence

Precedence is used to determine which medium is considered to 
occupy a volume when two or more media occupy the volume. The medium 
with the highest precedence value is considered to occupy the 
medium, 'displacing' the other media. 

The predefined and default scene medium, 'air', has precedence 
1. 

**type: ****integer** 

**unit**: 

**restrictions: **Should be > 1 

medium::epidermis
-----------------

Medium for simulating the outer layer of skin. 

See Jensen and Donner's paper for more details and example values. 

[http://graphics.ucsd.edu/papers/egsr2006skin/egsr2006skin.pdf](http://graphics.ucsd.edu/papers/egsr2006skin/egsr2006skin.pdf) 

### melanin_fraction

Fraction of melanin present in tissue. 

Typical range: 0 – 0.5 

**type: ****real scalar** 

**unit**: dimensionless 

**restrictions: **Should be in range [0, 1] 

### melanin_type_blend

Controls the amount of eumelanin relative to pheomelanim in 
the tissue. 

Typical range: 0 - 1 

**type: ****real scalar** 

**unit**: dimensionless 

**restrictions: **Should be in range [0, 1] 

medium::dermis
--------------

### hemoglobin_fraction

Controls the amount of hemoglobin present. 

Typical range: 0.001 – 0.1 

**type: ****real scalar** 

**unit**: dimensionless 

**restrictions: **Should be in range [0, 1] 

medium::basic
-------------

### ior

Index of refraction. Should be >= 1. 

Glass has an IOR (index of refraction) of about 1.5, water about 
1.33. 

The IOR of plastic varies, 1.5 would be a reasonable guess. 

type: scalar real 

unit: dimensionless 

restrictions: >= 1 

### cauchy_b_coeff

Sets the 'b' coefficient in [**Cauchy's equation**](http://en.wikipedia.org/wiki/Cauchy%27s_equation), 
which is used in Indigo to govern dispersive refraction. Units 
are micrometers squared. Setting to 0 disables dispersion. 
Note: the render can be slower to converge when dispersion is 
enabled, because each ray refracted through a dispersive medium 
can represent just one wavelength. So only set cauchy_b_coeff 
!= 0 if you really want to see dispersion :) 

Typical values for glass and water lie in the range 0.003 – 0.01 

(see [http://en.wikipedia.org/wiki/Cauchy%27s_equation](http://en.wikipedia.org/wiki/Cauchy%27s_equation) 
for some coefficients) 

**type: **scalar real 

**unit**: micrometers2 

**restrictions: **Should be >= 0 for physical correctness 

### absorption_coefficient_spectrum

Controls the rate at which light is absorbed as it passes through 
the medium. 

**type: ****spectrum element** 

**unit**: meter-1 

**restrictions: **Should be >= 0 for physical correctness 

### subsurface_scattering

Use this element to make the medium scatter light as it passes 
through it. 

{text:soft-page-break} element status: optional 

### subsurface_scattering::scattering_coefficient_spectrum

**type: ****spectrum element** 

**unit**: meter-1 

**restrictions: **Should be >= 0 for physical correctness 

### subsurface_scattering:: phase_function

Chooses the phase function used for the scattering. 

Should contain one phase_function element (see below). 

**type: ****phase function element** 

xml example: 

    <medium>
        <name>scattering_medium</name>
            
        <ior>1.5</ior>
        <cauchy_b_coeff>0.0</cauchy_b_coeff>
        <absorption_coefficient_spectrum>
            <rgb>
                <rgb>10000.0 5 5</rgb>
            </rgb>
        </absorption_coefficient_spectrum>
        
        <subsurface_scattering>
            <scattering_coefficient_spectrum>
                <uniform>
                    <value>10</value>
                </uniform>
            </scattering_coefficient_spectrum>
                
            <phase_function>
                <uniform/>
            </phase_function>
        </subsurface_scattering>
    </medium>

Phase Function 

The phase function controls in what direction light is scattered, 
when a scattering event occurs. 

Must be one of: 

### uniform

Takes no parameters 

xml example: 

    <phase_function>
        <uniform/>

</phase_function> 

### henyey_greenstein

The Henyey-Greenstein phase function can be forwards or backwards 
scattering, depending on the 'g' parameter. 

henyey_greenstein::g_spectrum 

The g parameter may vary with wavelength, and is therefore specified 
using a spectrum element. 

Spectrum values will be silently clamped to [-0.99, 0.99] . 

type: spectrum element 

units: dimensionless (average cosine of phase function scattering 
angle) 

restrictions: spectrum values should lie in range [-1, 1] 

xml example: 

    <phase_function>  {text:line-break}  <henyey_greenstein>  {text:line-break}  <g_spectrum>  {text:line-break}  <uniform>  {text:line-break}  <value>0.9</value>  {text:line-break}  </uniform>  {text:line-break}  </g_spectrum>  {text:line-break}  </henyey_greenstein>  {text:line-break} </phase_function> 

Spectrum
--------

Should have exactly one child, either peak, blackbody, rgb, 
or uniform. 

### spectrum::peak

### spectrum::peak::peak_min

The wavelength in nm of the start of the spectrum peak. 

type: real scalar 

units: nanometers 

restrictions: < peak_max 

### spectrum::peak::peak_width

The width of the spectrum peak, in nm. 

type: real scalar 

**units: **nanometers 

**restrictions: **> 0 

### spectrum::peak::base_value

Exitant radiance for wavelengths outside the peak part of the 
spectrum. 

type: real scalar 

units: spectral radiance, W m-3 sr-1 

restrictions: >= 0 

### spectrum::peak::peak_value

Exitant radiance for wavelengths inside the peak part of the 
spectrum. 

**type: **real scalar 

units: spectral radiance, W m-3 sr-1 

restrictions: >= 0 

### {text:soft-page-break} spectrum::blackbody

### spectrum::blackbody::temperature

**type: **real scalar 

units: Kelvin 

restrictions: > 0 

### spectrum::blackbody::gain

Exitant radiance is scaled by this 

**type: **real scalar 

**units: **dimensionless 

**restrictions: **> 0 

### spectrum::rgb

### spectrum::rgb::rgb

**type: **real 3-vector 

units: spectral radiance, W m-3 sr-1 

### spectrum::rgb::gamma

**The gamma value is used to convert rgb values from image values 
into intensity-linear display values.** 

**The rgb components are raised by this exponent.** 

**Use 2.2 as a suitable default.** 

**type: ****real scalar** 

units: dimensionless 

restrictions: must be > 0 

### {text:soft-page-break} spectrum::uniform

### spectrum::uniform::value

**type: **real scalar 

units: spectral radiance, W m-3 sr-1 

### spectrum::regular_tabulated

Allows nearly abitrary spectra to be defined. The spectrum value 
is given at regular wavelength intervals, and linear interpolation 
is used to sample at intermediate wavelengths. 

### spectrum::regular_tabulated::start_wavelength

**Wavelength of the first spectrum value.** 

**type: **real scalar 

**units: **meters. 

### spectrum::regular_tabulated::end_wavelength

**Wavelength of the last spectrum value.** 

**type: **real scalar 

**units: **meters. 

### spectrum::regular_tabulated::num_values

**Number of tabulated values** 

**type: ****integer** 

**units: ** 

xml example: 

      <material>
          <name>mat1</name>
     {text:soft-page-break}       <diffuse>
             <albedo_spectrum>
                <regular_tabulated>
                   <start_wavelength>0.4E-06</start_wavelength>
                   <end_wavelength>0.7E-06</end_wavelength>
                   <num_values>10</num_values>
                   <values>
                      1 0.9 0.5 0.345 0 0 0 0 0 0
                   </values>
                </regular_tabulated>
             </albedo_spectrum>
          </diffuse>
       </material> 

wavelength-dependent material parameter 

A wavelength-dependent material parameter may either by constant, 
in which case it does not vary spatially, or it may be controlled 
by a texture, or it may be controlled by a shader. 

A wavelength-dependent material parameter element must have 
exactly one child element, with the name 'constant', 'texture', 
or 'shader'. 

constant 

**A ****constant**** wavelength-dependent material parameter 
defines a material parameter that does not vary spatially. However, 
it can still vary with wavelength, so therefore a spectrum element 
is used to define the parameter.** 

**Type: ****spectrum element** 

**units: ****depends on context** 

texture 

**A ****texture**** wavelength-dependent material parameter 
defines a material parameter that is controlled by a texture 
map.** 

texture::texture_index 

**type: ****integer** 

**restrictions**: **must be the 0-based index of a texture defined 
in the current material.** 

shader 

**A ****shader**** wavelength-dependent material parameter 
defines a material parameter that is controlled by a shader program.** 

**For a wavelength-dependent material parameter, a shader 
program can be defined two different ways. In the first way, the 
shader is executed once for each wavelength. This allows the 
most control when creating wavelength-dependent parameters.** 

**To define a shader in this way, you must define a function called 
'eval' with signature and return type:** 

    **eval(real wavelen, vec3 pos) real {text:line-break} **

**In the second way, the shader is executed only once for all wavelengths, 
and returns a RGB 3-vector, that is in turn converted into a spectrum 
internally in Indigo.** 

**To define a shader in this way, you must define a function called 
'eval' with signature and return type:** 

    **def eval(vec3 pos) vec3**

{text:soft-page-break} shader::shader 

**type: ****string** 

**restrictions**: **must define a valid shader program.** 

wavelength-independent material parameter 

A wavelength-independent material parameter may either by 
constant, in which case it does not vary spatially, or it may be 
controlled by a texture, or it may be controlled by a shader. 

A wavelength-independent material parameter element must 
have exactly one child element, with the name 'constant', 'texture', 
or 'shader'. 

constant 

**A ****constant**** wavelength-independent material parameter 
defines a material parameter that does not vary spatially.** 

**Type: ****real scalar** 

**units: ****depends on context** 

texture 

**A ****texture**** wavelength-independent material parameter 
defines a material parameter that is controlled by a texture 
map.** 

texture::texture_index 

**type: ****integer** 

**restrictions**: **must be the 0-based index of a texture defined 
in the current material.** 

shader 

**A ****shader**** wavelength-independent material parameter 
defines a material parameter that is controlled by a shader program.** 

**To define a shader in this way, you must define a function called 
'eval' with signature and return type:** 

    **def eval(vec3 pos) real {text:line-break} **

shader::shader 

**type: ****string** 

**restrictions**: **must define a valid shader program.** 

displacement material parameter 

A displacement material parameter may either by constant, in 
which case it does not vary spatially, or it may be controlled 
by a texture, or it may be controlled by a shader. 

A displacement material parameter element must have exactly 
one child element, with the name 'constant', 'texture', or 'shader'. 

constant 

**Type: ****real scalar** 

**units: ****depends on context** 

texture 

**A ****texture**** displacement material parameter defines 
a material parameter that is controlled by a texture map.** 

texture::texture_index 

**type: ****integer** 

**restrictions**: **must be the 0-based index of a texture defined 
in the current material.** 

shader 

**A ****shader**** displacement material parameter defines 
a material parameter that is controlled by a shader program.** 

**To define a shader in this way, you must define a function called 
'eval' with signature and return type:** 

    **def eval() real {text:line-break} **

shader::shader 

**type: ****string** 

**restrictions**: **must define a valid shader program.** 

rectanglelight
--------------

The rectangle light element defines a horizontal area light 
with normal (0,0,-1). 

### pos

The (x, y, z) position of the middle of the rectangle area light. 

**type: **real 3-vector 

**units: **meters 

restrictions: 

### width

Width in x direction. 

**type: **real scalar 

**units: **meters 

restrictions: > 0 

### height

Width in y direction. 

**type: **real scalar 

**units: **meters 

**restrictions: **> 0 

### spectrum

Emission spectrum for the rectangle light; spectrum element 
is described above 

**type: ****spectrum element** 

### efficacy_scale

The efficacy_scale element allows light sources of a given wattage 
and efficacy to be simulated. 

The efficacy_scale element is optional, if it is used, it overrides 
the gain. Otherwise the gain works as {text:soft-page-break} 
normal. {text:line-break} {text:line-break} The overall 
luminous efficiacy is the luminous flux per Watt of power drawn. 
{text:line-break} There are some values on the wikipedia page 
[http://en.wikipedia.org/wiki/Luminous_efficacy](http://en.wikipedia.org/wiki/Luminous_efficacy) 

element status: optional {text:line-break} 

### efficacy_scale::power_drawn

**Power drawn by the light source, e.g. 100 Watts** 

**type: **real scalar 

**units: ****Watts** 

**restrictions: **> 0 

### efficacy_scale::overall_luminous_efficiacy

The overall luminous efficiacy is the luminous flux per Watt 
of power drawn. 

**type: **real scalar 

**units: ****Lumens per Watt (lm/W)** 

**restrictions: **> 0 

example xml: 

    <rectanglelight>
            <pos>0.0 0 1.9</pos>
            <width>0.2</width>
            <height>0.2</height>
                    
            <spectrum>
                    <peak>
                            <peak_min>300</peak_min>
                            <peak_width>550</peak_width>
                            <base_value>0</base_value>
                            <peak_value>200</peak_value>
                    </peak>
        </spectrum>
        
        <efficiacy_scale>  {text:line-break}         <power_drawn>100</power_drawn>  {text:line-break}         <overall_luminous_efficiacy>17.5</overall_luminous_efficiacy> {text:line-break}     </efficiacy_scale> 

</rectanglelight> 

exit_portal
-----------

Exit portals are useful for speeding up the rate of convergence 
of interior renderings, when the interior is lit by an environmental 
light source, such as the sun/sky model. 

Exit portals are placed over the openings between the interior 
and the exterior environment. These openings are the 'portals' 
in the scene. 

Exit portals make the rendering process more efficient, because 
paths passing through such openings can be more efficiently 
sampled when explicity marked with an exit portal. 

Requirements for exit portal usage: 

* If exit portals are present in the scene, then all openings 
  must be covered by exit portals. In other words, all possible 
  paths that start on the camera, and then travel through space 
  or a transparent object, and then escape out of the scene into 
  the environment, must be blocked by one or more exit portals. 

* The geometric normal (defined by triangle winding order) 
  of an exit portal mesh triangle, where reachable by some path 
  from the camera, must point into the interior of the scene. 
  (i.e. The front side of the mesh faces should be visible by the 
  camera) 



### pos

Translation applied to the mesh vertex positions, when transforming 
from object space into world space. This is also the origin of 
the object coordinated system in world coordinates. 

type: real 3-vector 

units: meters 

**restrictions: ** 

### scale

Uniform scale applied to the mesh vertex positions, when transforming 
from object space into world space. 

type: real scalar 

**units: **dimensionless 

restrictions: > 0 

### rotation

Optional element that defines a linear transformation that 
is applied to the mesh vertex positions, when transforming from 
object space into world space. 

Note that position vectors in Indigo are considered to be column 
vectors. 

{text:soft-page-break} As of Indigo 0.9, the orthogonality 
requirement on this matrix has been relaxed, the matrix now must 
merely be invertible. 

### rotation :: matrix

Defines a 3x3 matrix, in row-major format. 

**type: **real 3x3 matrix 

**units**: dimensionless 

**restrictions: ****Must be invertible.** 

### mesh_name

Name of a mesh object already defined in the scene file. 

****type******: ****string** 

XML example: 

     <exit\_portal>
        <pos>0.591146 0.361125 0.957886</pos>
        <scale>1</scale>
        <rotation>
          <matrix>
            1.000 0.000 0.000 0.000 1.0000 0.000 0.000 0.000 1.000
          </matrix>
        </rotation>
        <mesh\_name>Plane.011</mesh\_name>
      </exit\_portal>

meshlight
---------

NOTE: Meshlight is deprecated, use emitting materials instead. 

A mesh light is an emitter that uses triangle mesh geometry. Any 
mesh that has already been defined can be used to define a mesh 
light. 

### pos

Translation applied to the mesh vertex positions, when transforming 
from object space into world space. This is also the origin of 
the object coordinated system in world coordinates. 

type: real 3-vector 

units: meters 

**restrictions: ** 

### scale

Uniform scale applied to the mesh vertex positions, when transforming 
from object space into world space. 

type: real scalar 

**units: **dimensionless 

restrictions: > 0 

### rotation

Optional element that defines a linear transformation that 
is applied to the mesh vertex positions, when transforming from 
object space into world space. 

Note that position vectors in Indigo are considered to be column 
vectors. 

As of Indigo 0.9, the orthogonality requirement on this matrix 
has been relaxed, the matrix now must merely be invertible. 

### rotation :: matrix

Defines a 3x3 matrix, in row-major format. 

**type: **real 3x3 matrix 

**units**: dimensionless 

{text:soft-page-break} **restrictions: ****Must be invertible.** 

### mesh_name

Name of a mesh object already defined in the scene file. 

****type******: ****string** 

### spectrum

Emission spectrum for the mesh light; spectrum element is described 
above 

**type: ****spectrum element** 

### efficacy_scale

The efficacy_scale element allows light sources of a given wattage 
and efficacy to be simulated. 

The efficacy_scale element is optional, if it is used, it overrides 
the gain. Otherwise the gain works as normal. {text:line-break} 
{text:line-break} The overall luminous efficiacy is the luminous 
flux per Watt of power drawn. {text:line-break} There are some 
values on the wikipedia page [http://en.wikipedia.org/wiki/Luminous_efficacy](http://en.wikipedia.org/wiki/Luminous_efficacy) 

element status: optional {text:line-break} 

### efficacy_scale::power_drawn

**Power drawn by the light source, e.g. 100 Watts** 

**type: **real scalar 

**units: ****Watts** 

**restrictions: **> 0 

### efficacy_scale::overall_luminous_efficiacy

The overall luminous efficiacy is the luminous flux per Watt 
of power drawn. 

**type: **real scalar 

**units: ****Lumens per Watt (lm/W)** 

**restrictions: ****> 0** 

### {text:soft-page-break} texture

If this element is present, then the light emitted from the mesh 
light is modulated by an image map. 

**element\_status**: optional 

**type****: texture element** 

### ies_profile

If this element is present, then a directional distribution 
of light will be emitted from the emitter. 

The directional distribution is loaded from a file satisfying 
the ANSI/IESNA LM-63-2002 data system (IES) for describing 
photometric light distributions. 

If the ies_profile is present, then the spectral radiance of 
the emission spectrum will be scaled so that the light emits a 
luminous flux as defined in the IES file. 

When using an IES profile, each triangle of the mesh light will 
emit light with a directional distibution determined by the 
IES data, using the normal of the triangle as the 'principle direction'. 
{text:line-break} So you can make the triangle face in any direction 
and it will work just fine. {text:line-break} {text:line-break} 
When modelling a meshlight that will be used as an IES emitter, 
make sure it is completely flat, so that all triangle normals 
are the same. 

Only IES files of photometric type 'C' are supported. 

Only IES files with vertical angles starting at 0 degrees and 
ending at 90 degrees are supported. 

**element\_status**: optional 

### ies_profile :: path

Path to the IES file. Can be absolute or relative. If relative, 
the path is taken as relative to the scene base directory. 

**type: ****string** 

XML example: 

<meshlight> 

        <pos>0 0 2.4</pos>
        <scale>1</scale>
        <spectrum>
            <blackbody>
     {text:soft-page-break}             <temperature>3500</temperature>
                <gain>1</gain>
            </blackbody>
        </spectrum>
        <mesh_name>prism</mesh_name>
        
        <efficacy_scale>
            <power_drawn>150</power_drawn>
            <overall_luminous_efficacy>20</overall_luminous_efficacy>
        </efficacy_scale>

</meshlight> 

mesh
----

### mesh :: name

Name of the mesh 

**type: ****string** 

### mesh :: scale

Scales the vertex positions. 

**type: **real scalar 

**units: ****dimensionless** 

**restrictions: **> 0 

default value: 1.0 

### mesh :: normal_smoothing

Enables or disables shading normals. Shading normals are interpolated 
across triangles from vertex normals. If normal\_smoothing 
is false, geometric normals are used. 

**type: ****boolean** 

### mesh :: max_num_subdivisions

The maximum number of subdivisions that will be performed on 
a triangle. The actual number of subdivisions performed will 
depend on other subdivision parameters. 

The algorithm for deciding whether a triangle will be subdivided 
is as follows: 

if view_dependent: 

subdivide = 

num_subdivs < max_num_subdivs AND 

triangle in view frustrum AND 

screen space pixel size > subdivide_pixel_threshold AND 

(curvature >= curvature_threshold OR 

displacement_error >= displacement_error_threshold) 

else if not view dependent: 

subdivide = 

num_subdivs < max_num_subdivs AND 

(curvature >= curvature_threshold OR 

displacement_error >= displacement_error_threshold) 

{text:soft-page-break} **type: ****integer** 

**restrictions: **>= 0 

**default value: ****0** 

### mesh :: subdivide_pixel_threshold

Subdivision threshold in triangle screen-space pixels. 

**type: ****scalar real** 

****units: ******screen-space pixels** 

**restrictions: **>= 0 

**default value: **4.0 

### mesh :: subdivide_curvature_threshold

Subdivision curvature threshold. 

**type: ****scalar real** 

****units: ******radians** 

**restrictions: **>= 0 

**default value: **0.1 

### mesh :: displacement_error_threshold

Displacement error threshold. 

For example, if the displacement texture map specifies a displacement 
of 0.2 m in the center of a triangle, and the displacement_error_threshold 
is 0.1 m, then the triangle will be subdivided 

**type: ****scalar real** 

****units: ******meters** 

**restrictions: **>= 0 

**default value: **0.1 m 

### mesh :: view_dependent_subdivision

If true, the position of the object relative to the camera affects 
how much triangles are subdivided. 

**type: ****boolean** 

{text:soft-page-break} **default value: **true 

### mesh :: subdivision_smoothing

If true, the mesh is smoothed after subdivision takes place, 
i.e. Vertices are moved towards the limit surface. 

**type: ****boolean** 

**default value: **true 

### mesh :: merge_vertices_with_same_pos_and_normal

If true, all vertices sharing the same position and normal are 
merged, meaning that triangles adjacent to the pre-merge vertices 
are subsequently considered adjacent. 

**type: ****boolean** 

**default value: **true 

### mesh :: external

An external mesh type allows a mesh defined in another file to 
be loaded and used. 

### mesh :: external :: path

Path to mesh data file. 

Path can be absolute or relative. If relative, it is take as relative 
to the scene file base path. 

Allowed file types are .obj, .3ds, and .ply, .igmesh. 

**type: ****string** 

### mesh :: embedded

An embedded mesh type allows the mesh to be defined directly in 
the .igs file. 

### mesh :: embedded :: expose_uv_set

Names a given index of uv (texture) coordinate information. 
Materials can then bind to the uv coordinates using the given 
name. 

### mesh :: embedded :: expose_uv_set :: index

Index of the uv coordinates as defined in the embedded mesh data. 

**type: ****integer** 

{text:soft-page-break} **restrictions: **** must be >= 0, 
must be < than the total number of uv coordinates defined in the 
mesh data.** 

**unit**: dimensionless 

### mesh :: embedded :: expose_uv_set :: name

Name with which the uv set will be exposed to the materials. 

**type: ****string** 

**restrictions:** 

**unit**: 

### mesh :: embedded :: vertex

Defines a single vertex. 

### mesh :: embedded :: vertex :: pos (attribute)

Position of the vertex, in the local coordinate system of the 
mesh 

**type: ****real 3-vector** 

**restrictions:** 

**unit**: meters 

### mesh :: embedded :: vertex :: normal (attribute)

Normal of the vertex, in the local coordinate system of the mesh 

**type: ****real 3-vector** 

**restrictions: **** vector must be normalised (have length 
~= 1.0)** 

**unit**: meters 

### mesh :: embedded :: vertex :: uvN (attribute)

N-th uv coordinates. N must be >= 0 and <= 3. 

**type: ****real 2-vector** 

**restrictions: ** 

**unit**: normalised texture coordinates. 

### {text:soft-page-break} mesh :: embedded :: triangle_set

Defines a group of triangles sharing a common material. 

### mesh :: embedded :: triangle_set :: material_name

Name of the material triangles in this group will use. 

**type: ****string** 

**restrictions: ****must be the name of an already-defined 
material.** 

**Unit**: 

### mesh :: embedded :: triangle_set :: tri

Defines a single triangle in terms of its constituent vertices, 
as a 3-vector of vertex indices. 

The indices index into the vertices already defined in the current 
mesh. 

**type: ****integer 3-vector** 

**restrictions: ****each vertex index must be >= 0 and < the total 
number of vertices already defined for the current mesh.** 

**unit**: 

Xml example of an external mesh: 

<mesh> 

        <name>hand</name>
        <normal_smoothing>false</normal_smoothing>
        <scale>0.0005</scale>
        <external>
            <path>..\hand\gipshand2-273k.obj</path>
        </external>
    </mesh>
    
    

An example of an internally defined mesh: 

    <mesh>
        <name>mesh1</name>
        
        <normal_smoothing>false</normal_smoothing>
        <embedded>
            <expose_uv_set>
                <index>0</index>
                <name>albedo</name>
            </expose_uv_set>
                
     {text:soft-page-break}         <expose_uv_set>
                <index>0</index>
                <name>bump</name>
            </expose_uv_set>
            
            <vertex pos="-10 -10 0" normal="0 0 1" uv0="0 0" />
            <vertex pos="-10 10 0" normal="0 0 1" uv0="0 10" />
            <vertex pos="10 10 0" normal="0 0 1" uv0="10 10" />
            <vertex pos="10 -10 0" normal="0 0 1" uv0="10 0" />
                
            <triangle_set>                        
                <material_name>white</material_name>
                <tri>0 1 2</tri>
                <tri>0 2 3</tri>
            </triangle_set>
            
            <vertex pos="-10 3 0" normal="0 -1 1" uv0="0 0" />
            <vertex pos="-10 3 20" normal="0 -1 1" uv0="0 10" />
            <vertex pos="10 3 20" normal="0 -1 1" uv0="10 10" />
            <vertex pos="10 3 0" normal="0 -1 1" uv0="10 0" />
                
            <triangle_set>                        
                <material_name>checker</material_name>
                <tri>4 5 6</tri>
                <tri>4 6 7</tri>
            </triangle_set>
        </embedded>
    </mesh>
    

model
-----

Places a mesh instance into the scene. 

### pos

Translation applied to the model vertex positions, when transforming 
from object space into world space. This is also the origin of 
the object coordinated system in world coordinates. 

type: real 3-vector 

units: meters 

**restrictions: ** 

### scale

Uniform scale applied to the model vertex positions, when transforming 
from object space into world space. 

type: real scalar 

**units: **dimensionless 

restrictions: > 0 

### rotation

Optional element that defines a linear transformation that 
is applied to the model vertex positions, when transforming 
from object space into world space. 

Note that position vectors in Indigo are considered to be column 
vectors. 

As of Indigo 0.9, the orthogonality requirement on this matrix 
has been relaxed, the matrix now must merely be invertible. 

### rotation :: matrix

Defines a 3x3 matrix, in row-major format. For example, the identity 
matrix / null rotation can be defined like this: 

    <rotation>      
            <matrix> 1 0 0 0 1 0 0 0 1 </matrix> 

</rotation> 

**type: **real 3x3 matrix 

**units**: dimensionless 

{text:soft-page-break} **restrictions: ****Must be invertible.** 

### mesh_name

Name of a mesh object already defined in the scene file. 

****type******: ****string** 

### emission_scale

Scales the amount of light emitted by a certain material as applied 
to the current model, according to one of several different photometric 
measures. 

Element status: optional. 

emission_scale::material_name 

The name of a material. 

****type******: ****string** 

emission_scale::measure 

The following table gives the acceptable values for measure, 
in the name column: 

****type******: ****string** 

**emission\\_scale::value** 

**Defines the value of the corresponding measure.** 

****type******: ****real scalar** 

**units: ****dependent on the measure** 

**restrictions**: **> 0** 

### {text:soft-page-break} ies_profile

If this element is present, then a directional distribution 
of light will be emitted from the given material as applied to 
the current model mesh. 

The directional distribution is loaded from a file satisfying 
the ANSI/IESNA LM-63-2002 data system (IES) for describing 
photometric light distributions. 

If the ies_profile is present, then the spectral radiance of 
the emission spectrum will be scaled so that the light emits a 
luminous flux as defined in the IES file. 

When using an IES profile, each triangle of the mesh with the given 
material applied will emit light with a directional distibution 
determined by the IES data, using the normal of the triangle as 
the 'principle direction'. {text:line-break} So you can make 
the triangle face in any direction and it will work just fine. 
{text:line-break} {text:line-break} When modelling a meshlight 
that will be used as an IES emitter, make sure it is completely 
flat, so that all triangle normals are the same. 

Only IES files of photometric type 'C' are supported. 

Only IES files with vertical angles starting at 0 degrees and 
ending at 90 degrees are supported. 

**element\_status**: optional 

### ies_profile :: material_name

Name of the material which should emit light according to the 
IES profile. 

**type: ****string** 

### ies_profile :: path

Path to the IES file. Can be absolute or relative. If relative, 
the path is taken as relative to the scene base directory. 

**type: ****string** 

**xml example:** 

    **<model>**
    **    <rotation>**
    **        <matrix>**
    **            1 0 0 0 0 -1 0 1 0**
    **        </matrix>**
    **    </rotation>**
    **    <pos>0 0 0</pos>**
    **    <scale>1</scale>**
    
    **    <mesh\\_name>hand</mesh\\_name>**
    
    
     {text:soft-page-break} **        <material\\_name>mat1</material\\_name>**
    **        <measure>luminous\\_flux</measure>**
    **        <value>100000</value>**
    **    </emission\\_scale>**
    **</model>**
    

plane
-----

'Plane' is an infinite plane. 

Plane has been removed from Indigo. 

sphere
------

<img src='Pictures/100000000000025B0000027181896861.jpg' 
/> 

### sphere :: center

**type: **real 3-vector 

**units: **meters 

**restrictions:** 

### sphere :: radius

**type**: real scalar 

**units: **meters 

**restrictions**: > 0 

### sphere :: material_name

**type: **string 

**restrictions: **must be the name of an already specified material. 

Include
-------

The include element allows a different .igs file to be loaded 
and processed during the processing of the main .igs file. 

### include :: pathname

Path to another .igs file to be processed. Path is absolute or 
taken as relative to the current scene file directory. 

**type**: string 

**units: ** 

**restrictions**: 

**Indigo Shader Language Reference** 

### **Built-in types**

#### **real**

A real, scalar number, stored as a floating-point number. 

#### **int**

A 32-bit signed integer 

#### **bool**

A boolean value. 

#### **vec2**

A real 2-vector. 

#### **vec3**

A real 3-vector. 

#### **mat2x2**

A 2 x 2 real matrix. 

#### **mat3x3**

A 3 x 3 real matrix. 

### Literal values

Real literal values, integer and boolean literal values can 
be written with the syntax from C++, e.g. '-1.56e4', '4564', 
'true'. 

### Function Definitions

Functions are defined like so: 

    def myfunc(vec3 pos) vec3 :
    
     {text:soft-page-break}                                         fbm(pos, 10),
                                            sin(mul(doti(getTexCoords(0)), 100.0)),
                                            sin(mul(dotj(getTexCoords(0)), 100.0))
        )

The def keyword starts a function definition. Next is the name 
of the function, then the list of arguments to the function, where 
each argument name is preceeded by the argument type. Then the 
return type of the function follows. After the colon, the body 
of the function is defined. 

### Built-in functions – Conditional functions

#### **if(bool p, int a, int b) int**

#### **if(bool p, real a, real b)  real**

#### **...**

If p is true, returns a, otherwise returns b. 

### Built-in functions – Comparison functions

#### **eq(int a, int b) bool**

#### **eq(real a, real b) bool**

#### **...**

Returns true if a = b, false otherwise. 

#### **n****eq(int a, int b) bool**

#### **n****eq(real a, real b) bool**

#### **...**

Returns false if a = b, true otherwise. 

#### {text:soft-page-break} **lt****(int a, int b) bool**

#### **lt****(real a, real b) bool**

Returns a < b. 

#### **lte(int a, int b) bool**

#### **lte(real a, real b) bool**

Returns a <= b. 

#### **g****t(int a, int b) bool**

#### **g****t(real a, real b) bool**

Returns a > b. 

#### **g****te(int a, int b) bool**

#### **g****te(real a, real b) bool**

Returns a >= b. 

### Built-in functions – Boolean functions

#### **not(bool a) bool**

Returns ~a. 

#### **or(bool a, bool b) bool**

Returns a v b. 

#### **and(bool a, bool b) bool**

Returns a ^ b. 

#### **xor****(bool a, bool b) bool**

Returns a XOR b. 

### {text:soft-page-break} Built-in functions – Maths utility functions

#### add(real x, real y) real

#### add(int x, int y) int

#### add(vec2 x, vec2 y)  vec2

#### add(vec3 x, vec3 y)  vec3

Returns x + y. 

#### sub(real x, real y) real

#### sub(int x, int y) int

#### sub(vec2 x, vec2 y)  vec2

#### sub(vec3 x, vec3 y)  vec3

Returns x – y. 

#### mul(real x, real y) real

#### mul(int x, int y) int

Returns x * y. 

#### div(real x, real y) real

#### div(int x, int y) int

Returns x / y. 

#### mod(real x, real y) real

#### mod(int x, int y) int

Returns the remainder of x / y. 

#### {text:soft-page-break} sin(real x) real

Returns sin(x). 

#### asin(real x) real

Returns sin-1(x). 

#### cos(real x) real

Returns cos(x). 

#### acos(real x) real

Returns cos-1(x). 

#### tan(real x) real

Returns tan(x). 

#### atan(real x) real

Returns tan-1(x). 

#### abs(real x) real

#### abs(int x) int

Returns the absolute value of x. 

#### exp(real x) real

Returns ex. 

#### pow(real x, real y) real

Returns xy. 

#### sqrt(real x) real

Returns x1/2. 

#### {text:soft-page-break} log(real x) real

Returns the natural logarithm of x, ln(x). 

#### floor(real x) real

Returns the largest integer y, such that x >= y. 

#### ceil(real x) real

Returns the smallest integer y, such that x <= y. 

#### fract(real x) real

Returns x – floor(x). 

#### floorToInt(real x) int

Returns floor(x) converted to an integer. 

#### ceilToInt(real x) int

Returns ceil(x) converted to an integer. 

#### real(int x) real

Converts x to type real. 

#### min(int x, int y) int

#### min(real x, real y) real

#### min(vec2 x, vec2 y)  vec2

#### min(vec3 x, vec3 y)  vec3

If x < y, returns x, otherwise returns y. 

In the case of vec2 or vec3 arguments, the comparison is done component-wise. 

#### {text:soft-page-break} max(int x, int y) int

#### max(real x, real y) real

#### max(vec2 x, vec2 y)  vec2

#### max(vec3 x, vec3 y)  vec3

If x > y, returns x, otherwise returns y. 

In the case of vec2 or vec3 arguments, the comparision is done 
component-wise. 

#### lerp(real x, real y, real t) real

#### lerp(vec2 x, vec2 y, real t)  vec2

#### lerp(vec3 x, vec3 y, real t)  vec3

Returns x * (1 – t) + y * t 

#### clamp(int x, int minval, int maxval) int

#### clamp(real x, real minval, real maxval) real

#### clamp(vec2 x, vec2 minval, vec2 maxval)  vec2.

#### clamp(vec3 x, vec3 minval, vec3 maxval)  vec3

Returns max(minval, min(maxval, x)). 

In the case of vec2 or vec3 arguments, the clamping is done component-wise. 

Undefined if minval > maxval. 

### Built-in functions –  Vector constructors

#### vec2(real x, real y) vec2

Returns the 2-vector (x, y). 

#### {text:soft-page-break} vec2(real x) vec2

Returns the 2-vector (x, x). 

#### vec3(real x, real y, real z) vec3

Returns the 3-vector (x, y, z). 

#### vec3(real x) vec3

Returns the 3-vector (x, x, x). 

### Built-in functions –  Vector functions

#### dot(vec2 a, vec2 b) real

#### dot(vec3 a, vec3 b) real

Returns the dot product of **a** and **b.** 

#### cross(vec3 a, vec3 b) vec3

Returns the cross product of **a** and **b.** 

#### neg(vec3 a) vec3

Returns -**a**. 

#### length(vec2 a) real

#### length(vec3 a) real

Returns the length of **a**, ||**a**||. 

#### normalise(vec3 a) vec3

Returns **a** / ||**a**|| 

#### doti(vec3 a) real

Returns **i.a**, where** i** is the standard basis vector (1,0,0) 

#### {text:soft-page-break} dotj(vec3 a) real

Returns **j.a**, where** j** is the standard basis vector (0,1,0) 

#### dotk(vec3 a) real

Returns **k**.**a**, where** k** is the standard basis vector 
(0,0,1) 

#### doti(vec2 a) real

Returns **i.a**, where** i** is the standard basis vector (1,0) 

#### dotj(vec2 a) real

Returns **j.a**, where** j** is the standard basis vector (0,1) 

#### mul(vec2 a, real b) vec2

#### mul(vec3 a, real b) vec3

### Built-in functions – Matrix constructors

#### mat2x2(real e11, real e12, real e21, real e22) mat2x2

Returns the 2 x 2 matrix 

e11 e12 

e21 e22 

#### mat3x3(real e11, real e12, real e13, real e21, real e22, real e23, real e31, real e32, real e33) mat3x3

Returns the 3 x 3 matrix 

e11 e12 e13 

e21 e22 e23 

e31 e32 e33 

### {text:soft-page-break} Built-in functions – Matrix operations

#### mul(mat2x2 A, mat2x2 B)  mat2x2

Returns the 2 x 2 matrix **AB**. 

#### mul(mat3x3 A, mat3x3 B)  mat3x3

Returns the 3 x 3 matrix **AB**. 

#### mul(mat2x2 A, vec2 b) vec2

Returns the 2-vector (2 x 1 matrix) **Ab**. 

#### mul(mat3x3 A, vec3 b) vec3

Returns the 3-vector (3 x 1 matrix) **Ab**. 

#### transpose(mat2x2 A) mat2x2

#### transpose(mat3x3 A) mat3x3

Returns the transpose of **A**. 

#### inverse(mat2x2 A) mat2x2

#### inverse(mat3x3 A) mat3x3

Returns the inverse of **A**. Undefined if A is not invertible. 

### Built-in functions – procedural noise functions

#### noise(real x) real

Returns 1-D Perlin noise evaluated at x. 

#### noise(vec2 x) real

Returns 2-D Perlin noise evaluated at **x.** 

#### {text:soft-page-break} noise(vec3 x) real

Returns 3-D Perlin noise evaluated at **x.** 

#### fbm(real x, int oc) real

Returns oc octaves of 1-D Fractal Brownian Motion noise evaluated 
at x. 

#### fbm(vec2 x, int oc) real

Returns oc octaves of 2-D Fractal Brownian Motion noise evaluated 
at **x**. 

#### fbm(vec3 x, int oc) real

Returns oc octaves of 3-D Fractal Brownian Motion noise evaluated 
at **x.** 

### Built-in functions – texture sampling functions

#### getTexCoords(int texcoord_set_index) vec2

Gets the i-th texture coordinates at the shading point, where 
i = texcoord_set_index. 

#### sample2DTextureVec3(int texture_index, vec2 st) vec3

Samples the i-th texture defined in the current material, where 
i = texture_index is a 0-based index, at the normalised coordinates 
(s, t). Returns a (R, G, B) triplet, where each component will 
be in the range [0, 1]. 

### Built-in functions – debugging functions

#### print(real x) real

#### print(int x) int

#### ...

Prints the value of x to standard output, then returns it. Note 
that the print function is not guaranteed to execute in any particular 
order. 

Appendix A: Modelling a Liquid in a Glass For Indigo 

If you want to create a realistic rendering of a liquid in a glass 
vessel in Indigo, you must model it in a rather particular way, 
to take advantage of the medium precedence system, so that all 
light scattering and transmission processes are simulated 
(reasonably) accurately. 

In the requirements given below, a distance of 0.2mm is often 
mentioned. This distance is chosen because the default ray origin 
'nudge distance' (used to avoid false self-intersection due 
to limited floating point precision) in Indigo is 0.1mm. 

<img src='Pictures/100000000000040000000300F09A9BF8.png' 
/>Modelling Requirements: {text:line-break} {text:line-break} 
a) need sufficient polygonisation of the curve here because 
sharp edges cause shading normal artifacts. For example 10-20 
points may be needed on piecewise curve. {text:line-break} 
b) distance should be > 0.2mm {text:line-break} c) distance 
should be > 0.2mm. {text:line-break} Note that while the distance 
between the glass and **water** surfaces in the walls of the glass 
needs only to be greater than 0.2mm, it should probably be about 
1mm, depending on the width of the glass {text:line-break} d) 
distance between glass and ground plane should be in range [0.2mm, 
1mm] {text:line-break} e) meniscus should be modelled {text:line-break} 
{text:line-break} Addtionally: {text:line-break} {text:line-break} 
f) all geometric (given by tri winding order) and smoothed normals 
should be as labelled. {text:line-break} {text:soft-page-break} 
g) total number of triangles is expected to be in range 10000-150000 
{text:line-break} h) surfaces should be two-manifold and closed 
(not self-intersecting). {text:line-break} i) **liquid** 
and glass should be assigned different materials. {text:line-break} 
j) part of the surface of the **liquid** component should lie 
inside the glass as shown. {text:line-break} k) The model should 
be created in units of meters. 

l) The glass medium precedence should be greater than that of 
the **liquid** medium (because glass displaces water), which 
in turn should be greater than 1. 

The following image shows a wine glass half-profile modelled 
in MoI, which can easily be turned into a complete 3d model using 
a lathe/revolve modifier. 

Note how the lower and side edge of the wine volume lies inside 
the wall of the glass. 

<img src='Pictures/10000201000002310000040950B9241C.png' 
/> 

The wine glass rendered in Indigo: 

<img src='Pictures/100000000000025800000320A0FAABC1.png' 
/> 

