# Python CLP Wrapper 
# (c) Krzysztof Dorosz 
# 2008 AGH, dorosz@agh.edu.pl
# Wymaga biblioteki CLP ver. >=2.3 (mag)

from ctypes import *

CLPLIB = CDLL('/usr/local/clp/lib/libclp.so') # Ladowanie biblioteki CLP

def plp_init():
	"""Inicjalizuje biblioteke CLP"""
	CLPLIB.clp_init(1)

def plp_ver():
	"""Zwraca napis z numerem wersji CLP"""
	ver = create_string_buffer(80)
	CLPLIB.clp_ver(ver)
	return 'P'+ver.value[1:]

def plp_stat(pos):
	"""Zwraca statystyke czesci mowy w bibliotece CLP"""
	return CLPLIB.clp_stat(c_int(pos))

def plp_pos(id):
	"""Zwraca numer czesci mowy dla danego ID"""
	return CLPLIB.clp_pos(c_int(id))

def plp_label(id):
	"""Zwraca etykiete dla danego ID"""
	label = create_string_buffer(10)
	CLPLIB.clp_label(c_int(id), label)
	return label.value

def plp_bform(id):
	"""Zwraca forme podstawowa dla danego ID"""
	bform = create_string_buffer(80)
	CLPLIB.clp_bform(c_int(id), bform)
	return bform.value

def plp_forms(id):
	"""Zwraca liste form dla danego wyrazu"""
	formy = create_string_buffer(2048)
	CLPLIB.clp_forms(c_int(id), formy)
	return formy.value.split(':')[0:-1]

def plp_formv(id):
	"""Zwraca wektor form dla danego wyrazu"""
	wektor = create_string_buffer(2048)
	CLPLIB.clp_formv(c_int(id), wektor)
	return wektor.value.split(':')[0:-1]

def plp_vec(id, word):
	"""Zwraca wector odmiany"""
	out = Array50()
	num = c_int(0)
	CLPLIB.clp_vec(c_int(id), word, out, byref(num))
	return out[0:num.value]

def plp_rec(word):
	"""Zwraca liste numerow ID dla danego slowa"""
	Array50 = c_int * 50
	ids = Array50()
	num = c_int(0)
	CLPLIB.clp_rec(word, ids, byref(num))
	return ids[0:num.value]
	

