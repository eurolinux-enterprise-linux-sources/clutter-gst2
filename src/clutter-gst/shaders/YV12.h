/*
 * This file was generated by pso2h.
 */

#ifndef __YV12_H__
#define __YV12_H__

/*
 * This define is the size of the shader in bytes.  More precisely it's the
 * sum of strlen() of every string in the array.
 */
#define YV12_FP_SZ    564

static const char *YV12_fp[] =
{
  "!!ARBfp1.0\n",
  "PARAM c[2] = { { 1.1640625, 0.0625, 2.015625, 0.5 },\n",
  "{ 0.390625, 0.8125, 1.5976562 } };\n",
  "TEMP R0;\n",
  "TEMP R1;\n",
  "TEX R1.y, fragment.texcoord[0], texture[0], 2D;\n",
  "ADD R0.x, R1.y, -c[0].y;\n",
  "TEX R0.y, fragment.texcoord[0], texture[1], 2D;\n",
  "TEX R1.y, fragment.texcoord[0], texture[2], 2D;\n",
  "MUL R0.x, R0, c[0];\n",
  "ADD R0.w, R1.y, -c[0];\n",
  "MAD R0.z, R0.w, c[0], R0.x;\n",
  "ADD R0.y, R0, -c[0].w;\n",
  "MAD R0.w, -R0, c[1].x, R0.x;\n",
  "MAD R0.x, R0.y, c[1].z, R0;\n",
  "MAD R0.y, -R0, c[1], R0.w;\n",
  "MUL result.color.xyz, fragment.color.primary.w, R0;\n",
  "MOV result.color.w, fragment.color.primary;\n",
  "END\n",
  NULL
};

#endif
