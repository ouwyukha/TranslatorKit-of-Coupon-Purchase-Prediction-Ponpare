import pandas as pd

#Dataset Directory
dsdir = "./"

#Dataset
cd_train = pd.read_csv(os.path.join(dsdir,'coupon_detail_train.csv'))
cl_test = pd.read_csv(os.path.join(dsdir,'coupon_list_test.csv'))
cl_train = pd.read_csv(os.path.join(dsdir,'coupon_list_train.csv'))
cv_train = pd.read_csv(os.path.join(dsdir,'coupon_visit_train.csv'))
pref_loc = pd.read_csv(os.path.join(dsdir,'prefecture_locations.csv'))
sample_sub = pd.read_csv(os.path.join(dsdir,'sample_submission.csv'))
user_list = pd.read_csv(os.path.join(dsdir,'user_list.csv'))
coupon_area_train = pd.read_csv(os.path.join(dsdir,'coupon_area_train.csv'))
coupon_area_test = pd.read_csv(os.path.join(dsdir,'coupon_area_test.csv'))

#Translator
pref = pd.read_csv(os.path.join(dsdir,'pref.csv'),delimiter=';',index_col='jpn')
pref_office = pd.read_csv(os.path.join(dsdir,'pref_office.csv'),delimiter=';',index_col='jpn')
small_area_name = pd.read_csv(os.path.join(dsdir,'small_area_name.csv'),delimiter=';',index_col='jpn')
big_area_name = pd.read_csv(os.path.join(dsdir,'big_area_name.csv'),delimiter=';',index_col='jpn')
capsule_text = pd.read_csv(os.path.join(dsdir,'capsule_text.csv'),delimiter=';',index_col='jpn')
genre_name = pd.read_csv(os.path.join(dsdir,'genre.csv'),delimiter=';',index_col='jpn')

#CAPSULE TEXT
cl_test.CAPSULE_TEXT = cl_test.CAPSULE_TEXT.replace(capsule_text.to_dict()['en'])
cl_train.CAPSULE_TEXT = cl_train.CAPSULE_TEXT.replace(capsule_text.to_dict()['en'])

#GENRE NAME
cl_test.GENRE_NAME = cl_test.GENRE_NAME.replace(genre_name.to_dict()['en'])
cl_train.GENRE_NAME = cl_train.GENRE_NAME.replace(genre_name.to_dict()['en'])

#PREF NAME
cl_test.ken_name = cl_test.ken_name.replace(pref.to_dict()['en'])
cl_train.ken_name = cl_train.ken_name.replace(pref.to_dict()['en'])
pref_loc.PREF_NAME = pref_loc.PREF_NAME.replace(pref.to_dict()['en'])
user_list.PREF_NAME = user_list.PREF_NAME.replace(pref.to_dict()['en'])
coupon_area_train.PREF_NAME = coupon_area_train.PREF_NAME.replace(pref.to_dict()['en'])
coupon_area_test.PREF_NAME = coupon_area_test.PREF_NAME.replace(pref.to_dict()['en'])

#PREFECTUAL_OFFICE
pref_loc.PREFECTUAL_OFFICE = pref_loc.PREFECTUAL_OFFICE.replace(pref_office.to_dict()['en'])

#SMALL_AREA_NAME
cd_train.SMALL_AREA_NAME = cd_train.SMALL_AREA_NAME.replace(small_area_name.to_dict()['en'])
cl_test.small_area_name = cl_test.small_area_name.replace(small_area_name.to_dict()['en'])
cl_train.small_area_name = cl_train.small_area_name.replace(small_area_name.to_dict()['en'])
coupon_area_train.SMALL_AREA_NAME = coupon_area_train.SMALL_AREA_NAME.replace(small_area_name.to_dict()['en'])
coupon_area_test.SMALL_AREA_NAME = coupon_area_test.SMALL_AREA_NAME.replace(small_area_name.to_dict()['en'])

#large_area_name
cl_test.large_area_name = cl_test.large_area_name.replace(big_area_name.to_dict()['en'])
cl_train.large_area_name = cl_train.large_area_name.replace(big_area_name.to_dict()['en'])