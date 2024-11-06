import argparse
import netCDF4
import numpy as np
import os
import hashlib

# Reads in BUMP staticB correlation files and writes out at different resolution.


parser = argparse.ArgumentParser(
    description=('Read in BUMP correlation file and write out at a different resolution')
)
parser.add_argument(
    '-i', '--input',
    help="name of NetCDF input file",
    type=str, required=True)
parser.add_argument(
    '-o', '--output',
    help="name of NetCDF output file",
    type=str, required=True)
parser.add_argument(
    '-x', '--xdim',
    help="x-dimension",
    type=str, required=True)
parser.add_argument(
    '-y', '--ydim',
    help="y-dimension",
    type=str, required=True)
parser.add_argument(
    '-z', '--zdim',
    help="z-dimension",
    type=str, required=True)
parser.add_argument(
    "-sf", "--so4_flag",
    help="so4 tuning factor",
    type=str, required=False)
parser.add_argument(
    "-bc1f", "--bc1_flag",
    help="bc1 tuning factor",
    type=str, required=False)
parser.add_argument(
    "-bc2f", "--bc2_flag",
    help="bc2 tuning factor",
    type=str, required=False)
parser.add_argument(
    "-oc1f", "--oc1_flag",
    help="oc1 tuning factor",
    type=str, required=False)
parser.add_argument(
    "-oc2f", "--oc2_flag",
    help="oc2 tuning factor",
    type=str, required=False)
parser.add_argument(
    "-du1f", "--du1_flag",
    help="dust1 tuning factor",
    type=str, required=False)
parser.add_argument(
    "-du2f", "--du2_flag",
    help="dust2 tuning factor",
    type=str, required=False)
parser.add_argument(
    "-du3f", "--du3_flag",
    help="dust3 tuning factor",
    type=str, required=False)
parser.add_argument(
    "-du4f", "--du4_flag",
    help="dust4 tuning factor",
    type=str, required=False)
parser.add_argument(
    "-du5f", "--du5_flag",
    help="dust5 tuning factor",
    type=str, required=False)
parser.add_argument(
    "-ss1f", "--ss1_flag",
    help="seas1 tuning factor",
    type=str, required=False)
parser.add_argument(
    "-ss2f", "--ss2_flag",
    help="seas2 tuning factor",
    type=str, required=False)
parser.add_argument(
    "-ss3f", "--ss3_flag",
    help="seas3 tuning factor",
    type=str, required=False)
parser.add_argument(
    "-ss4f", "--ss4_flag",
    help="seas4 tuning factor",
    type=str, required=False)





args = parser.parse_args()



ncfile_in = netCDF4.Dataset(args.input, mode='r', format='NETCDF4')
ncfile_out = netCDF4.Dataset(args.output, mode='w', format='NETCDF4')

xdim = int(args.xdim)
ydim = int(args.ydim)
zdim = int(args.zdim)
print('args.so4_flag=',args.so4_flag)
fac_so4 = float(args.so4_flag)
fac_bc1 = float(args.bc1_flag)
fac_bc2 = float(args.bc2_flag)
fac_oc1 = float(args.oc1_flag)
fac_oc2 = float(args.oc2_flag)
print('args.du1_flag = ',args.du1_flag)
fac_dust1 = float(args.du1_flag)
fac_dust2 = float(args.du2_flag)
print('args.du3_flag = ',args.du3_flag)
fac_dust3 = float(args.du3_flag)
fac_dust4 = float(args.du4_flag)
fac_dust5 = float(args.du5_flag)
fac_seas1 = float(args.ss1_flag)
fac_seas2 = float(args.ss2_flag)
fac_seas3 = float(args.ss3_flag)
fac_seas4 = float(args.ss4_flag)

my_attrs = dict(filename=args.output)
for name, value in my_attrs.items():
    setattr(ncfile_out, name, value)


so4a = ncfile_in.variables['so4']
bc1a = ncfile_in.variables['bc1']
bc2a = ncfile_in.variables['bc2']
oc1a = ncfile_in.variables['oc1']
oc2a = ncfile_in.variables['oc2']
dust1a = ncfile_in.variables['dust1']
dust2a = ncfile_in.variables['dust2']
dust3a = ncfile_in.variables['dust3']
dust4a = ncfile_in.variables['dust4']
dust5a = ncfile_in.variables['dust5']
seas1a = ncfile_in.variables['seas1']
seas2a = ncfile_in.variables['seas2']
seas3a = ncfile_in.variables['seas3']
seas4a = ncfile_in.variables['seas4'] 



print('dims=',xdim,ydim,zdim)
xaxis_1 = ncfile_out.createDimension("xaxis_1", xdim)
xaxis_1 = ncfile_out.createVariable("xaxis_1", float, ('xaxis_1')) 
xaxis_1.long_name = 'xaxis_1'
xaxis_1.units = 'none'
xaxis_1.cartesian_axis = 'X'
yaxis_1 = ncfile_out.createDimension("yaxis_1", ydim)
yaxis_1 = ncfile_out.createVariable("yaxis_1", float, ('yaxis_1'))
yaxis_1.long_name = 'yaxis_1'
yaxis_1.units = 'none'
yaxis_1.cartesian_axis = 'Y'
zaxis_1 = ncfile_out.createDimension("zaxis_1", zdim) 
zaxis_1 = ncfile_out.createVariable("zaxis_1", float, ('zaxis_1'))
zaxis_1.long_name = 'zaxis_1'
zaxis_1.units = 'none'
zaxis_1.cartesian_axis = 'Z'
print('zaxis_1=',zaxis_1)
Time = ncfile_out.createDimension("Time",None )
Time = ncfile_out.createVariable("Time", float, ('Time'))
Time.long_name = 'Time'
Time.units = 'time level'
Time.cartesian_axis = 'T'
so4=ncfile_out.createVariable('so4', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
so4.long_name = 'mass_fraction_of_sulfate_in_air' 
so4.units = 'ugkg-1' 
so4.checksum = hashlib.md5("so4".encode('utf-8')).hexdigest()[:16]
bc1=ncfile_out.createVariable('bc1', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
bc1.long_name = 'mass_fraction_of_hydrophobic_black_carbon_in_air'
bc1.units = 'ugkg-1'
bc1.checksum = hashlib.md5("bc1".encode('utf-8')).hexdigest()[:16]
bc2=ncfile_out.createVariable('bc2', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
bc2.long_name = 'mass_fraction_of_hydrophilic_black_carbon_in_air'
bc2.units = 'ugkg-1'
bc2.checksum = hashlib.md5("bc2".encode('utf-8')).hexdigest()[:16]
oc1=ncfile_out.createVariable('oc1', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
oc1.long_name = 'mass_fraction_of_hydrophobic_organic_carbon_in_air'
oc1.units = 'ugkg-1'
oc1.checksum = hashlib.md5("oc1".encode('utf-8')).hexdigest()[:16]
oc2=ncfile_out.createVariable('oc2', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
oc2.long_name = 'mass_fraction_of_hydrophilic_organic_carbon_in_air'
oc2.units = 'ugkg-1'
oc2.checksum = hashlib.md5("oc2".encode('utf-8')).hexdigest()[:16]
dust1=ncfile_out.createVariable('dust1', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
dust1.long_name = 'mass_fraction_of_dust001_in_air'
dust1.units = 'ugkg-1'
dust1.checksum = hashlib.md5("dust1".encode('utf-8')).hexdigest()[:16]
dust2=ncfile_out.createVariable('dust2', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
dust2.long_name = 'mass_fraction_of_dust002_in_air'
dust2.units = 'ugkg-1'
dust2.checksum = hashlib.md5("dust2".encode('utf-8')).hexdigest()[:16]
dust3=ncfile_out.createVariable('dust3', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
dust3.long_name = 'mass_fraction_of_dust003_in_air'
dust3.units = 'ugkg-1'
dust3.checksum = hashlib.md5("dust3".encode('utf-8')).hexdigest()[:16]
dust4=ncfile_out.createVariable('dust4', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
dust4.long_name = 'mass_fraction_of_dust004_in_air'
dust4.units = 'ugkg-1'
dust4.checksum = hashlib.md5("dust4".encode('utf-8')).hexdigest()[:16]
dust5=ncfile_out.createVariable('dust5', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
dust5.long_name = 'mass_fraction_of_dust005_in_air'
dust5.units = 'ugkg-1'
dust5.checksum = hashlib.md5("dust5".encode('utf-8')).hexdigest()[:16]
seas1=ncfile_out.createVariable('seas1', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
seas1.long_name = 'mass_fraction_of_sea_salt001_in_air'
seas1.units = 'ugkg-1'
seas1.checksum = hashlib.md5("seas1".encode('utf-8')).hexdigest()[:16]
seas2=ncfile_out.createVariable('seas2', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
seas2.long_name = 'mass_fraction_of_sea_salt002_in_air'
seas2.units = 'ugkg-1'
seas2.checksum = hashlib.md5("seas2".encode('utf-8')).hexdigest()[:16]
seas3=ncfile_out.createVariable('seas3', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
seas3.long_name = 'mass_fraction_of_sea_salt003_in_air'
seas3.units = 'ugkg-1'
seas3.checksum = hashlib.md5("seas3".encode('utf-8')).hexdigest()[:16]
seas4=ncfile_out.createVariable('seas4', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
seas4.long_name = 'mass_fraction_of_sea_salt004_in_air'
seas4.units = 'ugkg-1'
seas4.checksum = hashlib.md5("seas4".encode('utf-8')).hexdigest()[:16]
#seas5=ncfile_out.createVariable('seas5', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
#seas5.long_name = 'mass_fraction_of_sea_salt005_in_air'
#seas5.units = 'ugkg-1'
#seas5.checksum = hashlib.md5("seas5".encode('utf-8')).hexdigest()[:16]

xaxis_1a = [] 
yaxis_1a = []
zaxis_1a = [] 
for k in range(1,xdim+1):
    xaxis_1a += [k] 
    yaxis_1a += [k]
for k in range(1,zdim+1):
    zaxis_1a += [k]
xaxis_1[:] = xaxis_1a[:]
yaxis_1[:] = yaxis_1a[:] 
zaxis_1[:] = zaxis_1a[:]

Time_a = []
Time_a = [1]
Time[:] = Time_a[:]


#print(yaxis_1)

so4[:] = so4a[:]*0+fac_so4
bc1[:] = bc1a[:]*0+fac_bc1
bc2[:] = bc2a[:]*0+fac_bc2
oc1[:] = oc1a[:]*0+fac_oc1
oc2[:] = oc2a[:]*0+fac_oc2
seas1[:] = seas1a[:]*0+fac_seas1
seas2[:] = seas2a[:]*0+fac_seas2
seas3[:] = seas3a[:]*0+fac_seas3
seas4[:] = seas4a[:]*0+fac_seas4
#seas5[:] = seas5a[:]
dust1[:] = dust1a[:]*0+fac_dust1
dust2[:] = dust2a[:]*0+fac_dust2
dust3[:] = dust3a[:]*0+fac_dust3
dust4[:] = dust4a[:]*0+fac_dust4
dust5[:] = dust5a[:]*0+fac_dust5


ncfile_out.close
