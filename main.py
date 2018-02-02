import urllib
import zipfile
import nottingham_util
import rnn

#collect the data from server
#url="http://www-etud.iro.umontreal.ca/~boulanni/Nottingham.zip"
#urllib.urlretrieve(url,'dataset.zip')

#read zip file and extract it to data folder
zip = zipfile.ZipFile(r'dataset.zip')
zip.extractall('data')

#build the model
nottingham_util.create_model()

#train the model created
rnn.train_model()
