import io
import urllib
from urllib.request import urlretrieve

triplets = []
dataset = "./dataset/"
def triplet_download(query_and_triplets,flag = 0):
	triplets_no = 0
	names = ["query","positive","negative"]
	for triplet in query_and_triplets:
		triplet_name = str((triplets_no))
		triplets_no += 1
		final_path = []
		for url,name in zip(triplet,names):
			try :
				urlretrieve(url,dataset+triplet_name+name+".jpg")
				final_path.append(dataset+triplet_name+name+".jpg")
			except urllib.error.HTTPError :
				flag = 1
			print(triplets)
		if flag == 0:
			triplets.append(final_path)
		flag = 0
	

def dataset_sampler(triplet_url_filename):
	with io.open(triplet_url_filename,"r+") as fp:
		lines = fp.readlines()
		lines = [lines[i] for i in range(len(lines)) if not i%4 == 0]
		triplets_url = [[lines[i],lines[i+1],lines[i+2]] for i in range(0,len(lines)-2,3)]
		return triplets_url

if __name__ == "__main__":

	triplets_url = dataset_sampler("query_and_triplets.txt")
	#print(triplets_url[:10])
	triplet_download(triplets_url)
	print(triplets)
	with io.open("triplets.txt","w+") as fp:

		for triplet in triplets:
			fp.write(",".join(triplet))
			fp.write("\n")

		fp.close()
