import sys
import os

from Crypto.Hash import SHA256

def calculate_hash(file_path, block_size):
	file_size = os.path.getsize(file_path)
	last_block_size = file_size % block_size
	print("Opening File: ", file_path, ";", file_size, "bytes; \n")

	fp = open(file_path, "rb")

	last_hash = ""
	for chunk in read_reversed_chunks(fp, file_size, last_block_size, block_size):
		sha256 = SHA256.new()
		sha256.update(chunk)
		if(last_hash):
			sha256.update(last_hash)
		last_hash = sha256.digest()

	fp.close()
	return last_hash

def read_reversed_chunks(file_object, file_size, last_chunk_size, chunk_size):
	iter = 0
	last_pos = file_size
	while last_pos > 0:
		size = chunk_size
		if(iter == 0):
			size = last_chunk_size

		file_object.seek(last_pos - size)
		data = file_object.read(chunk_size)
		if not data:
			break

		iter += 1
		last_pos -= size
		yield data

if __name__ == "__main__":
	block_size = 1024
	file_target = "target.mp4"
	hash_taret = ""
	file_check = "check.mp4"
	hash_check = "03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8"

	h0_check = calculate_hash(file_check, block_size)
	h0_check_hex = h0_check.encode("hex")
	print("calculate h0 for ", file_check, ":", h0_check_hex)

	h0_target = calculate_hash(file_target, block_size)
	h0_target_hex = h0_target.encode("hex")
	print("calculate h0 for ", file_target, ":", h0_target_hex)
