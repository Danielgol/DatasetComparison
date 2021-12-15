from test_sign_local import calculate


def comparison(path_1, path_2):
	text_file = open(path_1, "r")
	lines = text_file.readlines()
	lines = list(filter(('\n').__ne__, lines))

	first = []
	for line in lines:
		if "642" in line:
			break
		first.append(line)

	refs_first = list(map(lambda elem: elem.split('.')[0], first))
	hypotheses = list(map(lambda elem: elem.split('.')[1], first))



	text_file = open(path_2, "r")
	lines = text_file.readlines()
	lines = list(filter(('\n').__ne__, lines))

	second = []
	for line in lines:
		if "642" in line:
			break
		second.append(line)

	refs_second = list(map(lambda elem: elem.split('.')[0], second))

	calculate(hypotheses, refs_second)

	#with open('comparison.txt', 'w') as f:
	#	for i in range(len(frase)):
	#		f.write( str(frase[i])+":\n" )
	#		f.write( str(resultados_avg[i])+" ||| "+str(resultado_video[i]) )
	#		f.write("\n\n")