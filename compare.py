from test_sign_local import calculate

text_file = open("./results.txt", "r")
lines = text_file.readlines()
lines = list(filter(('\n').__ne__, lines))

video = []
for line in lines:
	if "642" in line:
		break
	video.append(line)

resultado_video = list(map(lambda elem: elem.split('.')[0], video))
frase = list(map(lambda elem: elem.split('.')[1], video))

text_file = open("./avg-aligned.txt", "r")
lines = text_file.readlines()
lines = list(filter(('\n').__ne__, lines))

avg = []
for line in lines:
	if "642" in line:
		break
	avg.append(line)
resultado_avg = list(map(lambda elem: elem.split('.')[0], avg))

# ESTUDAR O TSPNET PARA PEGAR O BLEU E O ROUGE DE CADA FRASE INDIVIDUAL
# PARA SABER QUAIS FRASES SÃO AS MELHORES

calculate(frase, resultado_avg)

#with open('comparison.txt', 'w') as f:
#	for i in range(len(frase)):
#		f.write( str(frase[i])+":\n" )
#		f.write( str(resultado_avg[i])+" ||| "+str(resultado_video[i]) )
#		f.write("\n\n")