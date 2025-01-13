#!/usr/bin/env python
import os
import subprocess as sp
import datetime as dt
import glob
import sys 
import readline 
#import xarray as xr

#grid='96'
#grid='12'
#zdim='127'
#xdim=grid
#ydim=grid
#stddev_tune='2'
#cor_rh_tune='1'
#cor_rv_tune='1'

param_file='rescale.param'

paramf = open(param_file)

#data=[line.rstrip('\n ') for line in paramf]
#grid= data[0] 
#zdim = data[1]
#stddev_tune = data[2] 
#cor_rh_tune = data[3] 
#cor_rv_tune = data[4] 
grids = paramf.readline(4)
grid = grids.strip()
paramf.readline()
zdims = paramf.readline(5)
zdim = zdims.strip()
print('zdim = ', zdim)
paramf.readline()
print('grid = ', grid)
xdim = grid
ydim = grid 
stddev_tune_so4_s = paramf.readline(4)
stddev_tune_so4 = stddev_tune_so4_s.strip()
print('stddev_tune_so4 = ', stddev_tune_so4)
paramf.readline()
stddev_tune_bc1_s = paramf.readline(3)
stddev_tune_bc1 = stddev_tune_bc1_s.strip()
print('stddev_tune_bc1 = ', stddev_tune_bc1)
paramf.readline()
stddev_tune_bc2_s = paramf.readline(3)
stddev_tune_bc2 = stddev_tune_bc2_s.strip()
paramf.readline()
stddev_tune_oc1_s = paramf.readline(3)
stddev_tune_oc1 = stddev_tune_oc1_s.strip()
paramf.readline()
stddev_tune_oc2_s = paramf.readline(3)
stddev_tune_oc2 = stddev_tune_oc2_s.strip()
paramf.readline()
stddev_tune_dust1_s = paramf.readline(3)
stddev_tune_dust1 = stddev_tune_dust1_s.strip()
paramf.readline()
stddev_tune_dust2_s = paramf.readline(3)
stddev_tune_dust2 = stddev_tune_dust2_s.strip()
paramf.readline()
stddev_tune_dust3_s = paramf.readline(3)
stddev_tune_dust3 = stddev_tune_dust3_s.strip()
paramf.readline()
stddev_tune_dust4_s = paramf.readline(3)
stddev_tune_dust4 = stddev_tune_dust4_s.strip()
paramf.readline()
stddev_tune_dust5_s = paramf.readline(3)
stddev_tune_dust5 = stddev_tune_dust5_s.strip()
paramf.readline()
stddev_tune_seas1_s = paramf.readline(3)
stddev_tune_seas1 = stddev_tune_seas1_s.strip()
paramf.readline()
stddev_tune_seas2_s = paramf.readline(3)
stddev_tune_seas2 = stddev_tune_seas2_s.strip()
paramf.readline()
stddev_tune_seas3_s = paramf.readline(3)
stddev_tune_seas3 = stddev_tune_seas3_s.strip()
paramf.readline()
stddev_tune_seas4_s = paramf.readline(3)
stddev_tune_seas4 = stddev_tune_seas4_s.strip()

paramf.readline()
print('zdim=',zdim) 
print('grid=', grid)
print('stddev_tune_so4',stddev_tune_so4)
print('stddev_tune_bc1=',stddev_tune_bc1)
print('stddev_tune_bc2=',stddev_tune_bc2)
print('stddev_tune_oc1=',stddev_tune_oc1)
print('stddev_tune_oc2=',stddev_tune_oc2)
print('stddev_tune_dust1=',stddev_tune_dust1)
print('stddev_tune_dust2=',stddev_tune_dust2)
print('stddev_tune_dust3=',stddev_tune_dust3)
print('stddev_tune_dust4=',stddev_tune_dust4)
print('stddev_tune_dust5=',stddev_tune_dust5)
print('stddev_tune_seas1=',stddev_tune_seas1)
print('stddev_tune_seas2=',stddev_tune_seas2)
print('stddev_tune_seas3=',stddev_tune_seas3)
print('stddev_tune_seas4=',stddev_tune_seas4)

#InRoot='/scratch1/NCEPDEV/da/Andrew.Tangborn/JEDI/staticb_files/lagged_stddev10_seas_fix/'
#InRoot_cor='/scratch1/NCEPDEV/da/Andrew.Tangborn/JEDI/staticb_files/lagged_stddev10_seas_fix/'
InRoot='/scratch1/NCEPDEV/da/Andrew.Tangborn/JEDI/staticb_files/bump_feb_stddev2/'
#InRoot='/scratch1/NCEPDEV/da/Andrew.Tangborn/JEDI/bump_barre/'
#InRoot_cor='/scratch1/NCEPDEV/da/Andrew.Tangborn/JEDI/bump_barre/'





#OutRoot='/scratch1/NCEPDEV/da/Andrew.Tangborn/JEDI/fv3-bundle_april26_2022/test_3dvar_gfs_aero_c96/Data/staticb_aero_c96_extend/'
#OutRoot='/scratch1/NCEPDEV/da/Andrew.Tangborn/JEDI/fv3-bundle_april26_2022/test_3dvar_gfs_aero_c96/Data/staticb_aero_c96_127lvl_stddev10/'
#OutRoot='/scratch1/NCEPDEV/da/Andrew.Tangborn/JEDI/staticb_files/lvl127/stddev2' 
#FV3Grid='/scratch1/BMC/gsd-fv3-dev/MAPP_2018/pagowski/fix_fv3/C'+grid

year=2021
month=2
day=27
hour=0
yyyymmdd = 20210227 

executable_stddev='python bump_stddev_rescale.py'


OutRoot='/scratch1/NCEPDEV/da/Andrew.Tangborn/JEDI/rescale_files_tmp/'
#OutRoot='/scratch1/NCEPDEV/da/Andrew.Tangborn/JEDI/bump_barre_127/'
#if stddev_tune_so4 != '1':
#     add_string = 'stddev'+str(stddev_tune)
#     add_string_s = add_string.strip()
#     OutRoot += add_string_s 

#OutRoot += '/'


#print('OutRoot=',OutRoot)
#isExist = os.path.exists(OutRoot)
#if not isExist:
#    os.makedirs(OutRoot)

os.popen('cp '+InRoot+'*.coupler* '+OutRoot+'/.') 

# copy coupler files


my_env = os.environ.copy()
my_env['OMP_NUM_THREADS'] = '4' # for openmp to speed up fortran call
#./viirs2ioda.x $validtime $fv3dir $infile $outfile

itile = 1
ntiles = 6

while itile <= ntiles:
  print('start of loop, itile = ', itile)

  str_stddev_input = str(yyyymmdd)+'.'+str(hour).zfill(2)+'0000.stddev.fv_tracer.res.tile'+str(itile)+'.nc'


  str_stddev_output = 'rescale.fv_tracer.res.tile'+str(itile)+'.nc'


  input_flag='-i'
  output_flag='-o'
  xdim_flag='-x'
  ydim_flag='-y'
  zdim_flag='-z'
  so4_flag='-sf'
  bc1_flag='-bc1f'
  bc2_flag='-bc2f'
  oc1_flag='-oc1f'
  oc2_flag='-oc2f'
  dust1_flag='-du1f'
  dust2_flag='-du2f'
  dust3_flag='-du3f'
  dust4_flag='-du4f'
  dust5_flag='-du5f'
  seas1_flag='-ss1f'
  seas2_flag='-ss2f'
  seas3_flag='-ss3f'
  seas4_flag='-ss4f'


  InDir = InRoot
  OutDir = OutRoot
  input_file_stddev = InDir+str_stddev_input
  output_file_stddev = OutDir+str_stddev_output
  print('output file = ', output_file_stddev)
#  args_stddev = ' '+input_flag+' '+input_file_stddev+' '+xdim_flag+' '+xdim+' '+ydim_flag+' '+ydim+' '+zdim_flag+' '+zdim+' '+so4_flag+' '+stddev_tune_so4+'  '+bc1_flag+' '+stddev_tune_bc1+' '+bc2_flag+' '+stddev_tune_bc2+' '+oc1_flag+' '+stddev_tune_oc1+' '+oc2_flag+' '+stddev_tune_oc2+' '+dust1_flag+' '+stddev_tune_dust1+' '+dust2_flag+' '+stddev_tune_dust2+' '+dust3_flag+' '+stddev_tune_dust3+' '+dust4_flag+' '+stddev_tune_dust4+' '+dust5_flag+' '+stddev_tune_dust5+' '+seas1_flag+' '+stddev_tune_seas1+' '+seas2_flag+' '+stddev_tune_seas2+' '+seas3_flag+' '+stddev_tune_seas3+' '+seas4_flag+' '+stddev_tune_seas4+' '+output_flag+' '+output_file_stddev
  args_stddev = (
    f" {input_flag} {input_file_stddev} {xdim_flag} {xdim} {ydim_flag} {ydim} {zdim_flag} {zdim} "
    f"{so4_flag} {stddev_tune_so4} {bc1_flag} {stddev_tune_bc1} {bc2_flag} {stddev_tune_bc2} "
    f"{oc1_flag} {stddev_tune_oc1} {oc2_flag} {stddev_tune_oc2} {dust1_flag} {stddev_tune_dust1} "
    f"{dust2_flag} {stddev_tune_dust2} {dust3_flag} {stddev_tune_dust3} {dust4_flag} {stddev_tune_dust4} "
    f"{dust5_flag} {stddev_tune_dust5} {seas1_flag} {stddev_tune_seas1} {seas2_flag} {stddev_tune_seas2} "
    f"{seas3_flag} {stddev_tune_seas3} {seas4_flag} {stddev_tune_seas4} {output_flag} {output_file_stddev}"
)
  cmd_stddev = executable_stddev+args_stddev
  print('before proc_stddev') 
  proc_stddev = sp.Popen(cmd_stddev,env=my_env,shell=True)
  print('after proc_stddev')

  itile = itile + 1 
  print('itile = ', itile) 
