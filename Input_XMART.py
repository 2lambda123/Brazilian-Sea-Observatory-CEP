import datetime, os

forecast_mode = 1
refday_to_start = 0 
number_of_runs = 4

#Data de início e fim se forecast_mode = 0
start = datetime.date(2023,4,5)
end = datetime.date(2023,4,6)

dirpath = os.getcwd()

exe_dir = (dirpath+"//Level_1//exe")
mohid_log = (exe_dir+"//Mohid.log")

boundary_conditions_dir = (dirpath+"//Level_1//GeneralData//BoundaryConditions")

#Define number of domains
number_of_domains = 1

#Define directories (comment when not applicable)
results_dir = [0]*number_of_domains
results_dir [0] = (dirpath+"//Level_1//res")
#results_dir [1] = (dirpath+"//Level_1//Level_2//res")

data_dir = [0]*number_of_domains
data_dir [0] = (dirpath+"//Level_1//data")

backup_dir = [0]*number_of_domains
#backup_dir [0] = (dirpath+"\Backup")
backup_dir [0] = (r"/home/guilherme.franz/bso/backup/mohid/CEP")

timeseries_backup = 0

convert2netcdf = 0
convert2netcdf_dir = (dirpath+"//Work//Hdf5toNetcdf")
convert_list = ["Hydrodynamic_2_Surface.hdf5", "WaterProperties_2_Surface.hdf5"]

#Tamanho mínimo do arquivo em Bytes
f_min_meteo = 1000000
f_min_hydro = 1000000
f_min_wp = 1000000

number_of_meteo = 2
dir_meteo = [0]*number_of_meteo
file_name_meteo = [0]*number_of_meteo

dir_meteo [0] = (r"/home/guilherme.franz/bso/backup/wrf/cptec")
file_name_meteo [0] = "wrf.hdf5"

dir_meteo [1]= (r"/home/guilherme.franz/bso/backup/gfs")
file_name_meteo[1] = "gfs.hdf5"


number_of_hydro = 2
dir_hydro = [0]*number_of_hydro
file_hydro = [0]*number_of_hydro

dir_hydro[0] = (r"/home/guilherme.franz/bso/backup/mohid/SC_PR_SP")
file_hydro[0] = "Hydrodynamic_2.hdf5"

dir_hydro[1] = (r"/home/guilherme.franz/bso/backup/mohid/SC_PR_SP")
file_hydro[1] = "Hydrodynamic_2_Surface.hdf5"

number_of_wp = 1
dir_wp = [0]*number_of_wp
file_wp = [0]*number_of_wp

dir_wp[0] = (r"/home/guilherme.franz/bso/backup/mohid/SC_PR_SP")
file_wp[0] ="WaterProperties_2.hdf5"

rivers = 0
dir_rivers = (r"/dados1/mohid/backup/QSDC/")

#Send ftp (No = 0 Yes = 1)
send_ftp = 0
server = ""
user = ""
password = ""
cwd = ""
ftp_list = ["Hydrodynamic_2_Surface.hdf5.nc", "WaterProperties_2_Surface.hdf5.nc","Hydrodynamic_2_Surface.hdf5"]

telegram_messages = 0
#TOKEN = "YOUR TELEGRAM BOT TOKEN"
#chat_id = "YOUR CHAT ID"
model_name = "CEP"
