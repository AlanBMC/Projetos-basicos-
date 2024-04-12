import re
import json

# Exemplo de texto
texto = """
about aproximadamente; quase; ao redor
sobre; a respeito de

above em cima, por cima
sobre; sob; acima de; mais acima; mais de; mais do que

accord acordo; convênio; harmonia
acordar; conceder; concordar, consentir

account conta (em informática -
também o contrato que dá o
direito de acesso ao provedor ou
à rede da Internet); o ato de
prestar de contas;
descrição; explicação
considerar; julgar; computar;
estimar

across de lado a lado; através de;
transversalmente; no outro lado
a caminho da; acima de

act ato; ação; lei
atuar; obrar; produzir; agir

action ação; efeito; gesto;
movimento; combate

ad anúncio
anno domini anno domini (abreviação - ad),
depois de Cristo

add acrescentar; juntar; adicionar

advance avançar; promover;
adiantar; antecipar
avanço; adiantamento;
progresso
cedo; avançado

affect afetar (doença); atingir;
comover

afraid receoso; medroso;
amedrontado

after depois; desde
depois; em seguida; conforme
depois que
depois, após

afterwards mais tarde

again de novo, novamente; outra vez

against contra; em frente

age idade; época; geração
envelhecer; fazer envelhecer

ago há tempos atrás

aid ajuda; apoio; socorro; assistência
ajudar; socorrer

air ar; atmosfera; aspecto; aparência
ar; atmosfera

all todo; tudo
tudo; todo, todos
totalmente; inteiramente
todos; todo mundo

allow permitir; deixar

almost quase

alone sozinho; único
só, solitário

along junto com
adiante

already já; agora mesmo

also também; além disso

although embora, ainda que

always sempre

ambition aspiração; ambição

among entre; no meio de; dentro

an um, uma

ancient antigo, velho, referente à
Antigüidade
ancião , velho, pessoa que viveu
na Antigüidade

and e; também

another outro; diferente
mais um; outro, outra

answer resposta; resultado
responder; replicar; comparecer

any algum; qualquer
de qualquer forma; qualquer um
alguém

anything qualquer coisa

appear aparecer; mostrar-se

appearance aparência; aspecto

archer arqueiro, besteiro

arch
astuto, esperto; principal

arm braço; ramo de árvore
armar-se; andar armado

army exército

around em volta; ao redor
por perto; em volta de

art arte

are
tu és (uso arcaico)

as como, enquanto, conforme

a medida que; em relação a

ask perguntar; convidar

at em; a; no, na; em casa de; por

attack ataque; agressão; investida
atacar; combater; agredir

attempt tentativa; esforço
tentar; empreender

attention atenção; cuidado ;
consideração

authority autoridade, senhorio;
poder, jurisdição; alto
funcionário do governo

away em outro lugar; longe
fora, de fora (de um jogo)


back costas; parte posterior; dorso;
jogador da defesa (futebol)
posterior
atrás; novamente; para trás
apoiar; impelir para trás


bad,worse,worst mal, perverso,
ruim; depravado; infeliz;
enfermo
mau, perverso, ruim, nocivo
pior, o pior
maldosamente

bank banco; beira, margem, borda,
orla; caixa registradora;
desnível; orvalho (também
neve); teclas; (informática)
banco de memória, conexão
para
unidade de memória
voar ou movimentar-se em
inclinação; empilhar

barbarian implacado, bárbaro
implacável, bárbaro

battle batalha; guerra
batalhar; lutar

be,was,been ser; estar; existir

bear,bore,born dar a luz
sustentar; tolerar; sofrer;
produzir; usar
urso

beautiful lindo/a , belo/a

beauty beleza

because porque

become,became,become se tornar;
se transformar; ser digno de;
assentar

bed cama; jazida; alicerce; fundo
plantar em cantos de jardim
(terraços); fixar, espetar

before antes; em frente; adiante
antes de
antes; na presença

begin,began,begun começar

behind atrás de; inferior a
atrás; atrasado
atrás

believe acreditar, crer

below abaixo, por baixo
debaixo de; inferior a

beneath debaixo, mais abaixo

besides além de
exceto, salvo

best o melhor; roupas festivas; de
qualidade superior
da melhor maneira

good
bom; agradável; excelente;
vantajoso; útil; virtuoso;
legítimo

best
superar, tirar melhor proveito de
better melhor; mais

good
bom; agradável; excelente;
vantajoso; útil; virtuoso;
legítimo

better
melhoria; vantagem; superior
melhorar

between entre; no meio
no meio de; faz parte de

beyond além; do outro lado
mais longe
o Além, o mundo vindouro

big grande; importante; grosso;
maturo

bind,bound,bind atar; amarrar;
obrigar

birth nascimento; origem; linhagem,
prole
bishop bispo (igreja), peão de xadrez

bit pedaço, parte; moedinha; gume
(de ferramenta); freio de cavalo

bite
morder; engolir a isca

BInary digiT
(informática) bit, algarismo
binário

black preto; negro
preto; sujo; zangado
pintar de preto, enegrecer;
confiscar a mercadoria

blood sangue; raça
causar sangramento, fazer
sangrar

blue azul; celeste
azul
colorir de azul; gastar dinheiro
(gíria)

boat barco; bote; canoa
navegar; remar

body corpo; pessoa; corporação

book livro; caderno; álbum
anotar; registrar; garantir a
compra

both ambos; juntos
ambos
tanto como; assim como

boy garoto, menino, rapaz;
empregado para pequenos
serviços

break,broke,broken quebrar;
romper; violar; interromper;
cancelar; falir
fratura; intervalo, trégua;
arrombo; oportunidade;
modificação; (informática)
passagem, final e começo de
uma parte nova no documento

bright brilhante; claro; lúcido;
resplandecente; perspicaz

bring,brought,brought trazer;
servir; causar; executar; induzir

british inglês (da Inglaterra)

brother irmão

business negócios; assunto;
comércio; profissão; local de
trabalho
negociável

but se; condição; contrariedade;
limite
somente; quase que
exceto; apenas
más; senão; porém
dizer "porém", dizer "más"

by por; a; em; pelo; sobre; de; com
perto de
por; a; em; pelo; sobre; de; com;
multiplicado por; perto

call chamada; comunicação (por
telefone); visita; convite; direito;
obrigação
chamar; convidar; convocar;
intimar; telefonar; visitar

camp campo; acampamento
acampar; levantar
acampamento; morar em
acampamento
antiquado, ridículo; afeminado,
bicha


can poder; saber; conseguir
caixa; lata; prisão
enlatar; preservar
capital capital ( de país); capital
(dinheiro); letra maiúscula
principal; magnífico, excelente

captain capitão; comandante de
navio; comandante; capitão
(jogo de futebol)
comandar, dirigir, estar à frente

care atenção, preocupação; cuidado;
precaução
ter cuidado; preocupar-se;
importar-se

carry carregar; transmitir; continuar
alcance (da arma de fogo);
transporte de barcos na terra;
ato de carregar

case acontecimento; caso; bolsa;
frase; situação; aclamação;
(gramática) relativo; cesta, caixa;
(informática) gabinete, caixa de
metal que
contém os componentes
internos do computador
encaixotar, encaixar

cast arremessar, jogar; derrubar;
sobrepujar; espalhar; computar;
calcular; moldar; imaginar; (no
teatro:) distribuir os papéis
o ato ou efeito de atirar ou
lançar; grupo de artistas; gesso;
estrabismo ligeiro

castle castelo; mansão; fortaleza
encastelar (xadrez); colocar num
castelo

cause causa, motivo, rasão; origem;
processo
causar, ocasionar, motivar;
induzir

century século, centúria

certain certo, exato; fixo
chance acaso, sorte; oportunidade;
probabilidade; risco; perigo
casual, inesperado

ter chance; arriscar
change mudança, variedade,
alteração; troco, moeda miúda
mudar, trocar, trocar dinheiro;
transformar

chapter capítulo; época; filial;
assembléia religiosa
character caráter, natureza,
personalidade; figura; sinal;
(informática) caractere,
apresentação digital de uma
letra alfabética, digito numérico
ou
símbolo especial

chief chefe; comandante; cabeça do
grupo
primeiro; principal; importante

child criança

christian cristão, qualidade daquilo
que se refere ao cristianismo ou
à cristandade
cristão, relativo ao cristianismo
ou à cristandade
Christian (nome próprio)

church igreja
rezar, orar
circumstance circunstância, motivo
botar numa situação

citizen cidadão

city cidade
civil civil, relativo ao cidadão; gentil,
generoso

clear deixar claro; limpar; justificar;
absolver
claro, transparente, nítido
evidentemente; totalmente
apagamento

close fechar; encerrar; terminar
fechado; perto; apertado
próximo
fechamento, conclusão, término;
área fechada; pátio, quintal; rua
sem saída

cold frio
frio; resfriado, gripe

come,came,come vir; chegar;

consentir; suceder; atingir o
orgasmo

command comando, ordem; controle
comandar, controlar, governar

common comum; casual; simples;
público; banal; vulgar
bens comuns; área pública

company companhia (militar ou
comercial); associação
complete completar, terminar
completo, perfeito

condition condição, situação;
preparo físico; situação social
condicionar; combinar; estipular
uma condição

conduct conduta, comportamento;
administração
conduzir, dirigir; administrar

confidence confidência, confissão,
segredo; crença, segurança

conquest conquista

consider considerar, tomar em
consideração, levar em conta
continue continuar

count contar; levar em conta;
calcular
contagem; consideração,
estimação; alegação, acusação;
questão; conde

country país; área; nação; aldeia;
campo; província
campestre; rural

courage coragem

course percurso, direção; curso;
porção; prato; série
fluir; caçar lebres

court pátio; corte judicial; palácio
real; a corte (real); recepção
fazer a corte a-, convidar

cover tampa; cobertura; coberta;
envelope; abrigo
envendar; cobrir; tapar; abrigar;
proteger; revestir

cross cruz; revés; tribulação
cruzar; atravessar; atormentar;
contradizer
zangado, nervoso; cruzado;
contrário

cry chorar; gritar; chamar
choro; grito; clamor

curious curioso; raro; estranho

cut,cut,cut  
corte; machucado; talho; golpe cortar; partir; reduzir; recortar; castrar cortado; picado; preparado; castrado

danger  
perigo

dark  
escuro; moreno; secreto; misterioso escuro, escuridão, penumbra

daughter  
filha

day  
dia

dead  
morto; imóvel; inativo; inanimado os mortos, os falecidos; fim (de algo) completamente; de repente; absolutamente

dear  
querido; caro; amado caro, querido por alto preço interjeição que expressa compaixão surpresa e tristeza

death  
morte; mortalidade; condenação eterna

declare  
declarar; afirmar; explicar

deep  
profundo profundamente profundidade

degree  
grau; classe; degrau; passo; graduação

democratic  
democrático (segundo os princípios da democracia, igualitário, que guarda ou resguarda os direitos do ser humano)

desire  
desejo; vontade; pedido desejar, pedir

determine  
determinar, estipular

die  
morrer, falecer; murchar; evaporar dado; cunho (de moeda, letra, brasão, etc)

different  
diferente; especial

difficult  
difícil

dignity  
dignidade

discover  
descobrir; revelar; manifestar

distance  
distância; afastamento; espaço; intervalo distanciar-se, afastar-se, manter distância

distant  
distante; afastado; longínquo

divine  
divino, celestial adivinhar; revelar padre

do,did,done  
fazer; funcionar; cuidar de ; parar; mostrar; jogar; enganar confusão; preceito ("faça-determinada coisa); fraude (gíria)

door  
porta, entrada

dorothy  
Dorothy (nome pessoal)

doubt  
dúvida, suspeita, incerteza duvidar, suspeitar, desconfiar

down  
desanimado; na fossa; para baixo; (informática) travado, inativado, quebrado, na rede significa que o computador está fora de operação abatido descida; penugem; rancor derrubar; derrotar; engolir em baixo, debaixo, abaixo

dr  
médico; doutor

draw,drew,drawn  
puxar; tirar; extrair; desenhar; descrever; traçar; adiantar-se; atrair sucção; atração; empate; loteria

due  
dívida; obrigação; imposto devido; que combina

duke  
duque (título da aristocracia)

duty  
responsabilidade, obrigação; imposto

each  
cada cada um

early  
cedo cedo; em breve

earth  
terra, pó; planeta terra; fio neutro de uma ligação elétrica enterrar; assentar

easily  
facilmente; absolutamente; indubitavelmente

east  
este, nascente, oriente, leste oriental oriente

easy  
fácil; confortável; cômodo; sociável facilmente; livremente; tranqüilamente

eat  
comer; destruir; devorar; mastigar

effect  
efeito; ação; conseqüência; realização efetuar

eight  
oito oitavo

either  
um dos dois também; tampouco um ou outro; este ou aquele

else  
além de outro

emperor  
imperador (rei)

empire  
império, reinado

end  
fim, final; extremidade; finalidade; morte terminar, concluir, acabar; matar

enemy inimigo, adversário

england Inglaterra (país da Europa)

english inglês; pessoa de

nacionalidade inglesa; a língua
inglesa
inglês, relativo à Inglaterra

enough para, suficiente
bastante
para (de parar)
bastante; suficiente

enter entrar; anotar; penetrar

equal igual, idêntico; capaz
igual, de igual valor
igualar; emparelhar; parecer
escape fuga; escapamento; escape
escapar, fugir; deixar escapar;
deixar-se aproveitar
especially  
especialmente

establish  
estabelecer; edificar, construir

europe  
Europa (um dos cinco continentes)

even  
mesmo que, até plano, raso; liso; regular planar; alisar; igualar

evening  
noite (primeiras horas), o anoitecer de noite

even  
planar; alisar; igualar

ever  
sempre, eternamente; em algum tempo; alguma vez

every  
cada, cada um; todos

everything  
tudo

evil  
mal; perversidade, maldade mal, diabólico; corrupto com maldade, com perversidade

example  
exemplo, modelo

except  
exceto, menos; menos que a não ser que excluir; se pôr em contra de

exclaim  
exclamar

exercise  
exercício; treinamento, treino; uso, utilização; ginástica exercitar; usufruir de-; fazer ginástica, exercitar-se, treinar-se; preparar, treinar

existence  
existência, ser; vida

expect  
esperar; aguardar; supor

experience  
experiência; experimento experimentar; tentar; experimentar; sentir

eye  
olho; visão olhar, observar

face  
face; rosto; careta; superfície; arrogância (gíria); aspecto; honra encarar, estar de fronte; direcionar-se a-; estar diante de-; recobrir, cobrir

fact  
fato; realidade; feito; prova (em direito)

fair  
leal, justo, honrado; bonito, belo; regula; moderado; claro; legível logicamente; totalmente; realmente feira; exposição

faith  
fé; crença; religião; crédito, confiança; fidelidade

faithful  
fiéis, público fiel (na religião) fiel; dedicado; exato; fiel ao original, confiável

fall  
cair; descer; abaixar-se; diminuir; ceder; morrer; abandonar queda; descida; degradação; cachoeira; tombo; queda de temperatura ou preços

family  
família familiar; de família

famous  
conhecido, famoso, ilustre, notável, afamado

far  
distante, remoto, afastado longe, distante; em alto grau; em grande parte; bem mais

fate  
destino; sorte; morte; destruição

father  
pai parir; reconhecer a paternidade; servir como um pai para-; inventar

fear  
medo; terror; suspeita; preocupação; receio temer, ter medo; desconfiar; recear; ter respeito a

feel,felt,felt  
sentir; perceber; experimentar; apalpar sensação, tato, impressão; sentido de realização, toque (gíria)

felt  
feltro débil, fraco, que se pode executar; feito de feltro, de feltro transformar em feltro; recobrir com feltro, revestir com feltro

feeling  
sentir; perceber; experimentar; apalpar

feeling  
sentimento, emoção, ternura, piedade, pena, compaixão sensível, terno, comovedor, tocante

foot,feet  
pé; sola do pé; base; sopé; pé (medida); infantaria; bordas (de folhas)

fell  
lançar por terra; cortar, derrubar (árvore); sobrecoser couro, pele de animal; pasto; bainha; corte de árvores, derrubada terrível, apavorante, cruel; destruidor; fatal, mortal

fellow  
companheiro, camarada; rapaz, indivíduo; sócio; membro da universidade; amigo do mesmo tipo; amigo para

few  
poucos; alguns; números; um número bem pequeno pouco, únicos, alguns pouco, únicos, alguns

field  
campo (também em informática); área limitada; área; (informática) campo, detalhe da informação no seu registro; área; quadra; formação de jogadores; campo de batalha; combate campo, campina botar em campo (time de futebol, por exemplo); recepcionar bola

fifty  
cinqüenta

figure  
número, dígito; figura, vulto; forma; personalidade; preço; estrutura corporal, silhueta; impressão; expressão; símbolo calcular; contar; esperar; ter esperança; fazer figura; tornar-se importante; simbolizar

fill  
encher, encher-se; saciar; obturar (dente); peencher; satisfazer-se; aviar (receita) fartura, abundância; quantidade satisfatória

finally  
finalmente, no final; enfim, até que enfim

find,found,found  
achar; encontrar; descobrir; julgar; prover, fornecer, abastecer; perceber, notar; resolver descoberta; achado

fine  
gentil; fino; agradável; belo, bonito; magnífico; excelente; admirável; puro bem; primorosamente; muito bem; perfeitamente multa multar; tornar-se delicado, tornar-se mais fino; suavizar; necessitar

fire  
fogo; incêndio, chama; tiro; fogueira; entusiasmo; ardor, paixão incendiar; queimar; atirar; demitir; empolgar-se; excitar; disparar; animar

first  
primeiro; começo, princípio; primeiro lugar; excelente (nota) primeiro primeiro; começo; antes de; pela primeira vez; antes de

five cinco, 5; quinteto
cinco, 5; quinto

fix determinar; consertar; arrumar;
preparar; fixar; estabelecer;
subornar; ordenar
má situação, grande problema,
"encrenca"(gíria); localização;
injeção de heroína (gíria)

follow seguir; ir atrás de,
acompanhar, vir depois de,
perseguir; suceder; imitar;
obedecer; compreender; resultar

food comida, alimento, sustento

footnote nota na margem da página
(também em informática);
(informática) apelo a nota ao pé
de uma página que aparece na
continuação do texto
acrescentar notas ao pé de
página

for para, com o intuito de; por; pelo;
durante; apesar de; quanto a; a
favor; em relação; por causa; em
troca
porque, pois, já que

force poder, força, energia; eficácia;
causa, motivo; violência; tropa
forçar; obrigar; determinar;
exigir; pressionar; empurrar à
força; retirar à força; irromper,

fender
foreign estranho; estrangeiro;
diferente; exterior (política,
comércio, ministério)

forest floresta
florestar

form forma; personagem; formulário
(também em informática); forma
física; estado de espírito; classe;
cerimônia; comportamento;
arrumação; ordem;
(informática) formulário
formar; fabricar; consolidar; ser;
transformar-se; ordenar-se;
preparar-se; vestir-se de; criar-se

former prévio, anterior; antigo,
ancestral; primeiro, original; formador, ; molde, matriz

forth adiante; avante; em seguida;
para fora
fortune sorte, fortuna; boa sorte,
sucesso; riqueza, propriedades,
bens; demasiado caro; acaso;
destino

forty quarenta

forward mandar, transferir; adiantar;
(informática) passar adiante,
mandar uma mensagem de
correio que foi previamente
recebida
adiante, avante, ‘a frente; que
progrediu, avançado, adiantado;
pronto, entusiasmado;
prepotente, ousado; fronteiro,
frontal; futuro
adiante; avante; para frente, à
frente

four quatro, 4
quatro, 4; quarto

free livre; independente; liberto;
acessível; vago; grátis;
voluntário; imune
gratuitamente; livremente
liberar; livrar; resgatar;
privilegiar; desentupir; esgotar;
eximir
freedom liberdade, imunidade,
franquia; facilidade;
atrevimento; isenção
french francês, cidadão da França
francês, da França
frequent freqüente
friend amigo, companheiro,
conhecido; protetor; amigo do
peito
from de; desde; por
front frente, fachada; rosto, testa,
cara; começo, início;
atrevimento; caminho à
beira-mar; frente de batalha
anterior, precedente, dianteiro;
porta da frente
dirigir-se em direção a-, estar
diante de-, avistar, observar;
ousar
adiante, para a frente
full cheio; completo; satisfeito
direto, diretamente; muito, bem
totalidade
pisoar (pano)
further promover, favorecer,
facilitar; avançar
mais distante, mais adiante; um
outro, mais um
adiante, mais distante; além;
fora disto, além disto, também
future futuro
futuro; para o futuro; que vem,
próximo, vindouro
general geral, universal; comum
geral; general
generally geralmente;
ordinariamente
gentleman cavalheiro
german alemão (idioma)
alemão, cidadão da Alemanha
alemão , da Alemanha
german
(parente) de primeiro grau; do
mesmo pai e mãe
germany Alemanha (país europeu)
get,got,got receber; conseguir; obter;
adquirir; pegar (doença);
entender; chegar; causar;
induzir; decorar; procriar;
buscar
girl garota; menina; moça; mulher
(gíria)
give,gave,given dar; entregar,
conceder; render-se; premiar;
pagar; enfraquecer-se; preparar
(festas, etc)
flexibilidade
glass vidro; copo; cristal; óculos; (de
forma menos usada: tudo que é
feito de vidro como espelho,
lente, etc)
de vidro; vidraça
espelhar, refletir; enquadrar
(fotografia)
glory glória; honra; estima; respeito;
deferência; beleza
gloriar-se; glorificar-se
go,went,gone ir; viajar; chegar;
partir; caminhar; marchar;
mover-se
tentativa; energia; atividade
(gíria); moda
partido; quebrado; perdido;
destruído; foi; morreu
god Deus, o Eterno, o Todo Poderoso
gold ouro
de ouro; dourado; feito de ouro
good,better,best bom; agradável;
excelente; vantajoso; útil;
virtuoso; legítimo
utilidade; proveito; bom ;
vantagem
bem, de forma boa
government governo; regime;
comando
gradually gradualmente,
gradativamente, aos poucos
great,greater,greatest grande;
importante; imenso; volumoso;
notável; incrível
greek grego (idioma)
grego, da Grécia
grego, da Grécia
green verde (cor); campo de golfe;
verdura
verde; novato; fresco; recente;
tolo; viscoso
ground terra; chão, solo; território,
região; fundamento, base;
motivo, causa; terras, bens
aterrar; dar base; fundar,
fundamentar; detalhar
terra; chão; solo; terreno;
território
grind
triturar; pulverizar; afiar;
amolar; ralar; esfregar; ranger os
dentes; persistir (nos estudos)
hair cabelo; pelo
half metade, meio; (no futebol)
médio
meio, quase
meio
hand mão; letra de mão;
mão-de-obra; mão (num jogo de
cartas); operário, trabalhador;
marujo
dar, entregar, passar; ajudar
feito a mão
happen acontecer, suceder
happy feliz, alegre
hard duro, rude, severo
duramente; esforçadamente
have ter; possuir; receber; pegar;
necessitar; causar
rico, que tem muitas riquezas
he masculino, macho
ele
head cabeça; (informática) o
dispositivo que lê e escreve a
informação nos drives
conduzir, encabeçar; cabecear
principal, o mais importante
hear escutar, ouvir
heart coração
heaven paraíso; céu
heavy pesado; grande; grosso; forte
pesadamente
hold,held,held segurar; alimentar;
guardar; pensar; acreditar;
organizar; preparar; presidir
posse; custódia; influência
help ajuda; apoio; ajudante;
empregado
ajudar; contribuir; apoiar; curar;
consertar
her ela; lhe, a
here aqui; neste lugar; neste ponto,
cá
herself ela própria; ela mesma; a si
mesma; si própria; se
high alto, grande, elevado; superior;
digno; embriagado, drogado
altamente, a grande altura
altura; elevação; marcha alta;
recorde
him ele; lhe, o
himself ele próprio; ele mesmo; a si
mesmo; se
his dele, seu
history história
holy sagrado, santo
sagrado, sacro
home casa, lar
para casa; em casa; a bordo
caseiro, familiar, interno
ficar em casa; voltar
honor honra, respeito
honrar; cumprir
hope esperança, expectativa
ter esperança, esperar
horse cavalo (também em ginástica
olímpica)
cavalgar; levar nas costas;
montar a cavalo
hour hora; tempo
house casa; teatro; assembléia
residir, morar; hospedar-se,
hospedar
how como, de que modo, de que
forma
however de qualquer forma
como ?
human humano, ser humano
hundred cem
husband marido
economizar, poupar; casar,
desposar
idea idéia; pensamento; opinião;
intenção
if se; possibilidade; condição
se; mesmo que; embora; ainda
que; no momento que
ill enfermo, doente; mau, ruim,
daninho
desgraça, maldade; prejuízo,
dano; doença
dificilmente; de má forma;
maldosamente; com hostilidade
immediate imediato; direto; sem
intermediários, sem
interferências; realizado já
imperial imperial, real
moeda de ouro da Rússia
Imperial; pequena barba à moda
de Napoleão III
important importante; de valor;
arrogante
impossible impossível;
impraticável, irrealizável
in interno, interior; popular; na
moda; com poder de influência
dentro; em casa; na moda,
"in"(gíria); época (frutas, etc)
em, a, por, para, com, de,
durante, dentro de
pessoa do partido dirigente;
dono de posição de poder;
influência, manobra política
inch polegada (medida); bagatela,
insignificância
avançar devagar,
movimentar-se por polegadas
indeed realmente, de fato,
verdadeiramente, sem dúvida
realmente!deveras!
influence influência; poder,
autoridade; crédito; influxo
(eletricidade)
influenciar; ativar
inhabitant habitante; inquilino
instance instância; urgência;
exemplo; solicitação;
encorajamento
instead em lugar, em vez de
interest interesse; vantagem;
proveito, lucro, ganho; juro;
utilidade; poder; afeição
interessar, importar
into em, dentro de , para o interior
is ser; estar; existir
island ilha; isolado no texto
formar ilha; espalhar ilhas;
isolar (numa ilha)
it ele, ela, o, a; isto, isso; aquilo
itself para si próprio, se, sigo, si
mesmo
journey jornada, viajem, caminhada;
passagem, caminho
viajar, trajetar, excursionar
judge juiz; julgador; perito,
conhecedor
julgar, sentenciar; criticar,
decidir
julian juliano (relativo a Júlio César)
just justo, honesto; correto,
adequado, verdadeiro; virtuoso;
reto; imparcial
justamente, neste momento,
exatamente; quase, quase que
não, mais ou menos; somente;
dificilmente; precisamente
duelo entre cavaleiros nobres
justice justiça; retidão, justeza; lei;
julgamento; juíz
keep,kept,kept guardar; ficar;
cumprir; sustentar; deixar;
continuar; dirigir; criar; possuir
sustento, manutenção,
economia; forte, fortaleza
kind espécie; gênero; qualidade
bom, afável, maneiroso;
benévolo; humano; agradável;
bom coração; trata bem;
confortável
king rei
reinar; dominar; agir como um
rei
King
King (nome; Martin Lutter, o
maior líder negro dos E.U.A.)
kingdom reino; império; região;
reino
know,knew,known saber; conhecer;
entender; perceber; ter
conhecimento
reconhecido, sabido, declarado
knight cavaleiro; nobre
nomear título de coragem
knowledge saber, conhecimento;
cultura; inteligência
lady mulher, senhora, dama, dona
de casa; esposa
sexo feminino, mulher
lay,laid,laid leigo, secular, profano,
colocado, posto, estendido,
deitado
lay
pôr, meter, colocar, estender,
enterrar, deitar, acalmar,
aquietar, aplacar; ordenar,
mandar; traçar, projetar
land terra; pátria; nação; reino;
região; povo; nação; país;
território
desembarcar; pôr em terra;
aportar; descarregar; aterrar;
aterrizar; chegar (lugar,
situação)
language linguagem, idioma, língua
large grande; enorme; largo;
volumoso; vasto; amplo; grosso;
bombástico
liberdade, ausência de limites
last último; passado, que passou
(dias, semanas, etc); final,
derradeiro
ultimamente; a última vez; nos
últimos tempos; no final;
finalmente
continuar, permanecer; fazer a
tempo; sobreviver; agüentar;
perseverar
último; fim; forma de sapato;
extremidade; força de vida; last
(unidade de peso ou capacidade
de navio)
late atrasado; atraso; último; novo;
falecido; que faleceu
ultimamente; recente
tarde; ultimamente; há pouco;
até ultimamente; até um certo
ponto; até uma certa hora
later atrasado; atraso; último; novo;
falecido; que faleceu
ultimamente; recente
later
mais tarde
mais tarde; tempos após
latin latim (idioma clássico
difundido no Império Romano)
latino, cidadão da antiga Roma,
nascido num país latino
latino; dos povos latinos; do
idioma latino
latter o segundo, o citado em
segundo lugar, o citado por
último; o mais tardio
law lei; direito; justiça; regra;
constituição; foro; advocacia;
demanda; processo
lead,led,led conduzir, guiar,
comandar, pilotar, levar, dirigir;
governar; dominar-se;
capitanear
liderança, direção; diferença;
líder, condutor; orientação;
exemplo; direção tomada numa
investigação, pista; primeiro
lugar; papel
principal; ator principal;
corrente para cães
o mais importante, o primeiro;
líder, diretor; inaugurador,
inicial
chumbo; contém chumbo
chumbo; grafite; projétil (na
arma); peso, prumo; tabuleta de
chumbo (na imprensa)
learn,learnt,learnt estudar;
aprender; descobrir;
informar-se; decorar
least o mínimo, a menor quantidade
no menor grau, no mais baixo
grau, menos
o menor, o mínimo
leave,left,left deixar; largar; sair;
separar-se; abandonar; cessar;
desistir de; renunciar a
férias; permissão, autorização;
permissão para ausentar-se,
licença; despedida, partida
dar folhas, dar folhagem
left esquerda; lado esquerdo; a
esquerda
canhoto; esquerdo
a esquerda
Left
esquerda (política)
length comprido, longo, dilatado,
prolixo, pedaço (de pano)
less uma quantidade menor; o
inferior
menor; menos; inferior
menos
menos
sem
let,let,let deixar; permitir; dar;
alugar; fretar; conceder;
descobrir
apartamento para alugar;
aluguel; obstáculo; lance não
válido em jogo de raquetes e
que deve ser repetida
letter carta; letra; significado literal;
literatura, boa literatura
marcar com letras, rotular
liberty liberdade; permissão, licença;
imunidade; familiaridade; férias
life vida; alma; animal; espírito;
atividade; biografia; prisão
perpétua (gíria)
de vida; para toda a vida
light luz; iluminação; luz do dia;
relâmpago; fogo; fósforo; farol;
inteligência; inspiração

leve; pouca caloria; alegre;
cabeça aberta (gíria)
iluminado; claro
clarear; acender; queimar;
descer (do carro, etc); cair
(escolha); pousar; acontecer
like gostar; satisfazer; desejar
provavelmente; a maneira que;
”assim”, ”como se ” (gíria)
como; como se; por exemplo;
parece com; vale a ; igual a
exatamente como; assim como;
como se
parecido; semelhante; os seus
semelhantes; como-, conforme-
(aparece em palavras
compostas)
line linha; fila; limite; ramo; linha de
ação; corda; programa;
profissão; descrição
encarreirar; demarcar; sinalizar;
marcas com linhas; estender;
fortificar; forrar; encher (bolso)
little pouco; pequena quantidade;
pequena distância; pouco tempo
de maneira nenhuma;
escassamente
pequeno; pouco; curto; sem
valor; feto
live viver; morar; existir; sobreviver;
sustentar-se
vida; cheio de energia; cheio de
vida; iluminante; elétrico; ao
vivo
ao vivo
long longo, comprido
comprido; longo; improvável
(chances); distante
por muito tempo; há muito
tempo; durante muito tempo
desejar, apetecer; ter saudades,
ter lembranças nostálgicas
longer comprido; longo; improvável
(chances); distante
look olhar; aparência; vista;
semblante; aspecto; personagem
olhar, ver; enxergar; mostrar-se;
parecer-se; procurar
lord Deus, criador; senhor; dono;
lorde; amo; monarca,
governador
governar, controlar; agir com
arrogância; liderar como senhor
loss perda; ruína; fracasso; quebra;
desperdício
lose,lost,lost perder; desperdiçar;
arruinar; gastar; sofrer perdas;
escapar de-; não entender
lost
perdido; derrotado; sumido;
arruinado; disperso; absorto,
concentrado (em pensamentos)
love amor; amado, querido; afeição;
pessoa amada; zero pontos (no
jogo de tênis)
amar; gostar; adorar;
apaixonar-se; querer muito
low baixo; fraco; deprimido;
canalha; perdido; barato; sujo;
rude
barato; baixo; em voz baixa;
humildemente; vilmente
nível baixo; algo baixo; mugido
de vaca; balido
mugir
lower baixo; fraco; deprimido;
canalha; perdido; barato; sujo;
rude
lower
mais baixo, inferior
abaixar, rebaixar; diminuir;
humilhar, desdenhar, desprezar;
anuviar, nublar; obscurecer-se,
tornar sombrio
magic mágica; bruxaria; milagre
mágico, maravilhoso
make,made,made fazer; criar;
causar; tornar
fabricação, tipo
man homem; pessoa; marido;
tripulante de um navio; peão (
num jogo de dama ou xadrez)
guarnecer; tripular; equipar;
apoiar
manner maneira, jeito, modo;
costume, hábito; gênero,
espécie; delicadeza
many muito; bastante
muitos; vários
march março (terceiro mês do ano)
march
marcha, caminhada, desfile,
parada; passeata; avanço,
distância de uma caminhada;
limite, setor
caminhar; caminhar na
multidão; desfilar; participar de
uma passeata; conduzir uma
multidão; limitar
marriage casamento, matrimônio,
boda, núpcias
marry casar; unir; desposar; ajuntar,
aliar; casar-se
master senhor; controlador,
governante; professor, diretor
de escola; senhor de escravos;
mestre em alguma arte;
especialista; o jovem de uma
família (tratamento respeitoso)
controlar; sobrepujar; dominar
(um assunto ou atividade);
adquirir habilidade num certo
assunto ou atividade
principal; controlador, chefe;
especialista, hábil
matter matéria, corpo, substância;
assunto; negócio; importância;
quantidade
importar, interessar; ser
importante, ser significativo
may talvez; possível; pode ser;
provável; tomara
tipo de planta; época de
florescência
me mim; eu; para mim
mean pensar; significar; ter em vista;
tencionar; pretender; querer
dizer
meio, recurso; média
média; meio; mau, malvado;
pobre, miserável; sovina, "pão
duro"; inferior, de segunda
categoria
measure meio; medida; escala;
aparelho de medição; ritmo;
peso; medida legal, lei
medir; avaliar; destinar um
orçamento, dividir de acordo
com uma medida
meet,met,met encontrar;
encontrar-se; reunir-se; receber;
conhecer; abastecer
adequado, apropriado, digno,
merecedor
encontro; local de uma reunião
(de caçadores, etc)
memory memória (também em
informática); lembrança;
recordação; (informática)
memória, a região principal e a
mais rápida para o
armazenamento de
dados no computador
man,men homem; pessoa; marido;
tripulante de um navio; peão (
num jogo de dama ou xadrez)
mention mencionar, notar, aludir;
lembrar
menção; lembrança; indireta
merit mérito; valor; prêmio; virtude;
destaque
merecer, ser digno de
middle no meio, meio, metade
do meio, médio, central;
intermediário
mile milha terrestre (1.609, 35
metros); milha marítima (aprox.
1.853, 25 metros); longa
distância
military militar
mind mente; cérebro; alma;
pensamento; memória; opinião;
intenção; vontade
prestar atenção; considerar;
notar; vigiar; recordar; observar;
impugnar; lembrar; contrariar
mine meu
extrair; explorar; minar
mina; jazida; bomba
minute minuto, instante, nota,
anotação, rascunho, resumo,
apontamento
pequeno; diminutivo;
insignificante; meticuloso; para
preparo imediato (carne)
minutar
miss senhorita; moça
miss
errar; perder; atrasar; sentir
saudades; sentir falta; evitar (a
alguem)
erro (do alvo), perda; fracasso;
distanciamento, esquiva
modern moderno, novo, recente
moderno, novo
moment momento, instante, minuto,
tempo presente, importância;
gravidade
money dinheiro
month mês
more mais
mais; acréscimo; maior
(quantidade)
morning manhã, madrugada, aurora
de manhã
most o maior; a maioria; o principal;
o mais
o maior; a maioria; o principal; o
mais; quase (gíria)
mais; principalmente; quase
(gíria)
mother mãe; madre
materno
servir de mãe paramountain montanha, cordilheira,
serra
mouth boca
expressar, exprimir; balbuciar;
enfiar na boca
move mover; mexer; levar; passar;
mudar (de apartamento);
causar; propor; comover
movimento; proposição; ação;
mudança; jogada, movimento
(em xadrez); fila (jogo)
mr míster, senhor, seu, dom
mrs senhora, dona
much muito; bastante; grande
quantidade
muito; muito mais; bastante; em
grande quantidade
muito; muito mais; bastante; em
grande quantidade
must dever; ter necessidade; precisar
obrigação; imposição; suco de
uva; necessário
my meu
ai!(interjeição)
myself eu; a mim mesmo; para mim;
eu mesmo; a mim
name nome; apelido; anúncio;
autoridade; diploma
nome; fama, título; aparência;
poder; autoridade
com boa reputação; famoso; de
nome
nation nação; estado, país
national nacional; patriótico; público
native nativo, nascido; cidadão local
nativo, original do local, relativo
ao lugar de nascimento; de
nascença; natural; local
natural natural; relativo à natureza
natural; pessoa que possui dom
natural para um certo trabalho
(gíria); verdadeiro; idiota;
bastardo
nature natureza; gênio; caráter;
espécie; qualidade; naturalidade
Nature
natureza, universo
near perto; intimo; dos últimos
tempos; pão duro (gíria);
canhoto; o mais perto
perto; quase
perto de; perto a
aproximar
nearly perto, quase
necessary necessário; preciso;
essencial; decisivo
coisa necessária; coisa
indispensável
neck nuca; ousadia
need precisar, necessitar; carecer de
necessidade; precisão, carência;
pobreza
negro negro
de pele negra; negro; dos negros
neither nenhum, nenhum dos dois
nenhuma coisa
never nunca; jamais
new novo; recente; moderno; fresco
ultimamente; novamente
next o próximo; o breve
depois; na próxima vez
night noite; escuridão
noturno; de noite
nine nove, 9
nono
no não; não tem
não; sem
não; voto contra
de forma alguma; negativa
noble nobre; pertence a nobreza
nobre; honroso; correto
non não; não ter
none nenhum; de forma alguma
ninguém; de jeito nenhum; nada
nor nem
north
norte
north norte
nortista
not não; mesmo que não
note nota; bilhete; sinal; tom; marca;
lembrete; aviso
notar; anotar, apontar, registrar
nothing nada; zero; coisa alguma
nada; coisa alguma
now agora
já; neste momento
visto que, agora que; ora
number número; algarismo;
quantidade; multidão
contar, numerar, computar
numb
dormente; paralisado
numerous numeroso, múltiplo;
muito
object objeto, coisa, matéria;
assunto, objetivo, finalidade
objetar, impedir, opor-se,
imputar; aduzir
observe observar; notar; guardar;
cumprir (preceitos); cuidar dos
detalhes, ser detalhista; fazer
uma observação ou uma
colocação
obtain obter; receber; comprar,
adquirir; conseguir, conquistar
occasion ocasião, chance,
oportunidade; evento,
acontecimento; caso; razão
ocasionar; produzir; causar;
mover; excitar
of de; sobre; (pertencente) a
off desligado; fechado; cancelado;
lateral (estrada); livre (dia, etc);
afastado
fora; longe; ao largo
de; fora de; sob
fora !
estar "fechado", estar
"desligado"(em relação a
aparelhos, etc)
offer oferta; orçamento; expressão de
, demonstração de (boa vontade,
coleguismo, etc.)
ofertar, oferecer; orçar; servir;
demonstrar, expressar (boa
vontade, disposição)
office serviço; escritório; secretaria,
ministério
often frequentemente; muitas vezes
old velhos
idade; tem- (relacionado a
idade, tem 21 anos)
velho; antigo; idoso; veterano;
do passado
on ligado; aceso
em cima; adiante;
sucessivamente
em; sobre; no, na; por; de
once uma vez, uma só vez, em outro
tempo, antigamente
logo que, sempre que, uma vez
que
uma vez
one um; unidade
um; único; só
alguém; algum (a); aquele (a)
only só; único; raro
somente; unicamente; só
mas; portanto
open abrir; descobrir; destampar;
iniciar; inaugurar; ficar (de olho
em alguém); rachar; cortar;
aumentar; romper
aberto; descoberto; livre; vago
(trabalho); franco; exposto
lugar aberto; aberto; livre
opinion opinião, juízo, acordo,
conceito, reputação
or ou; seja
order ordem, mandato; regra;
preceito; costume; convite
convidar; ordenar; arrumar;
mandar; dirigir
ordinary normal
padre, indivíduo que possui
ofício dentro da igreja
original original, genuíno; legítimo
other outro (a); o outro
outro; diferente; segundo
diferentemente
outro, outros
ought dever, tornar-se necessário;
convir
our nosso
out fora; algo que está fora da vista
exterior; fora (num jogo); longe;
ausente ( da escola ou trabalho);
desligado; engano
de fora; para fora; até o final;
completamente
fora de ; fora
para fora
over novamente: ao lado; do outo
lado; demasiadamente; outra
vez
em cima de; por cima de; sobre;
durante
demais; mais; em excesso; mais
de ; superior
câmbio (chamada
radiotelegráfica)
own particular; ser dono; pertencer a
meu (seu, dele), para mim
oz onça (medida de peso inglesa
equivalente a 28, 349 g)
pain dor; mágoa; sofrimento
causar dor; afligir
palace palácio
paris Paris (capital da França)
part parte; região; posição; lado
(num contrato)
parte, pedaço
partido, dividido
separar, apartar; separar-se;
dividir
particular particular
especial; fora do normal;
especificado; detalhado;
detalhista
party festa; bando; partido;
destacamento; reunião
de festa; do partido;
comemoração
participar de uma festa (gíria);
beber álcool em grupo (gíria)
pass passar; transmitir; deixar,
permitir
passagem, caminho; trecho;
sorte na prova; salto conduto;
retirada da bala
passage passagem; parte; parágrafo
past passado; história; tempo
passado
passado; decorrido; transato
anterior; no passado; que
passou
acima de; depois que
patient paciente; doente, enfermo
paciente, que tem paciência;
calmo
pay pagar; saldar; satisfazer
salário, pagamento
peace paz; tranquilidade; calma
peculiar peculiar; estranho; especial;
raro
people pessoas; seres humanos;
povo; população; nação
encher de pessoas; povoar
perfect perfeito; sem defeito;
completo
aperfeiçoar; melhorar;
completar; fazer de forma
perfeita
perhaps talvez, quiçá, quem sabe,
possivelmente
period período, época, tempo, era
menstruação, época do ciclo
mensal, período menstrual
período, época; ponto (para fim
de frase); fim, conclusão; frase
completa
person pessoa; ser; indivíduo;
personagem
personal pessoal; particular
notícias locais; notícia sobre
uma pessoa no jornal
peter Pedro (nome pessoal); Pedro
(apóstolo de Cristo)
peter
definhar; exaurir; consumir-se
place lugar; local; posição; situação;
emprego
instalar; colocar; pôr;
estabelecer; plantar
plain plano; campina; planície
simples; leal; sincero; comum;
verdadeiro
simplesmente; francamente;
claramente
pleasure agrado; satisfação; prazer
point ponto (também em
informática); principal;
propósito; interesse;
(informática) ponto, medida
pequena usada para medir
fontes
apontar; pontuar; assinalar;
indicar
political político, relativo à política
poor pobre; miserável; coitado;
infeliz
pobre
popular popular; amado, apreciado;
aceito; comumente encontrado
position posição; localização; local;
emprego; trabalho;
posicionamento, estado,
situação
colocar; instalar
possess possuir; controlar; reter,
segurar
possession posse, possessão; bem,
propriedade; controle
possible possível
pound libra (moeda); libra (peso);
tapada; curral; pancada forte;
golpe
encurralar; moer; triturar;
golpear; espancar; estudar
muito
power poder; energia; força;
domínio; superioridade; força
(eletricidade)
a motor; mecânico
fornecer energia; movimentar
powerful potente; poderoso; forte
presence presença; aparecimento
present presente; tempo presente;
favorável
presente; lembrança
existe; presente; agora; atual
apresentar; conceder; oferecer;
demonstrar; mostrar
pretty bonito, belo; legal
lindo; elegante; de bom
tamanho; bem grande; gentil
embelezar, enfeitar
pride orgulho; amor próprio;
vaidade; respeito de si mesmo
orgulhar-se
prince príncipe; governante
private privado; pessoal; particular
soldado raso
probably provavelmente
produce gerar; criar; produzir
(filme); motivar; apresentar;
fabricar; frutificar; dar resultado
produção; produto; fruto
progress progresso; adiantamento
progredir; adiantar
proof evidência; prova; dureza;
firmeza
fortalecer; imunizar; obstruir;
fechar; corrigir; revisar
prova; ensaio; evidência;
firmeza
property propriedade, posse; bens;
terras; qualidade, característica;
peça, parte
prove provar; mostrar; tentar;
demonstrar; verificar
province província; distrito;
ocupação
public público; o povo
público; geral
purpose propósito; intento;
finalidade; objetivo; alvo
tencionar
put,put,put colocar; pôr; enfiar;
sinalizar; situar; propor; oferecer
ressoar causado por bala de
ferro
queen rainha; soberana;
homossexual (gíria)
question questão; pergunta;
problema; assunto; controvérsia;
debate; dúvida
perguntar; interrogar; examinar;
; duvidar; discutir; recusar
quickly depressa; rapidamente;
vivamente
quite totalmente; completamente;
absolutamente; perfeitamente;
inteiramente; muito; bastante
race corrida; sexo; raça; saída
correr, participar de uma corrida
raise levantar; construir; causar;
educar
elevação, levantamento,
aumento
rank nível; posto; estado social;
camada; linha; série
colocar em ordem; graduar;
ordenar
grosseiro, violento
rather de preferência; especialmente;
particularmente
reach alcançar; atingir; estender
(mão)
alcance; extensão
read,read,read ler; aprender;
aconselhar; avisar; estudar;
interpretar
leitura
ready pronto, preparado; útil; breve;
ágil
preparar
pronto !
real real; verdadeiro; prático; realista
verdadeiro e genuíno
realidade, verdade
really realmente; de verdade;
seriamente
reason razão; entendimento; causa;
motivo; argumento
pensar, considerar; justificar
receive receber; aceitar; admitir;
acolher; entender; perceber
red vermelho
vermelho; rubor; vermelhidão;
comunistas; índio americano
reduce reduzir, diminuir, cortar
regard reparar; observar; respeitar;
estimar
respeito, honra; consideração
reign reino, reinado, império
dominar, reinar
religion religião; fé
religious religioso
(os) religiosos
remain ficar
remember lembrar; relembrar;
recordar-se
remove remover, retirar, tirar
remoção, transferência; subir de
sala; fase; despesa, gasto
reply resposta, reação, contestação
responder; replicar; contestar
report relatório, relato; notícia,
informação; reportagem
relatar; informar
respect respeito, apreço;
consideração
respeitar
rest resto; troco; descanso; férias;
parada; sono
descansar; dormir; cessar; dar
descanso
result resultado
resultar, terminar em
return volta; retorno; espaço;
recompensa; (informática) tecla
return ou enter
retorno; devolver; regressar
regresso; volta, retorno, de
volta, chegada, vinda
rich rico; valioso; farto; profundo;
delicioso
(os) ricos
right direito; correto; certo; justo;
ajustado
diretamente; em linha reta;
exatamente
direito; mão direita; direita;
justiça
estar certo
Right
direita (política)
river rio
road estrada; caminho; trilho de
ferro
robin pintarroxo (ave)
Robin
Robin (nome próprio)
roman papal, católico; romano
Roman (nome próprio); relativo,
originário ou pertencente a
Roma; pertencente ou relativo a
Igreja Apostólica Romana
(Igreja Católica)
rome Roma (capital da Itália; nome
do império de Julios Cesar)
room quarto; alojamento
alojar
rose levantar; subir; elevar-se;
erguer-se
rose
rosa; cor-de-rosa; roseira;
chuveiro; erisipela
rosa
round volta, roda; esfera; ciclo
redondo
em volta
a volta
arredondar, circular, contornar
royal real
run,ran,run corrida; distância;
marcha; viagem; jornada;
derrota; série; falha (na meia)
correr; fugir; executar; executar
um programa (informática);
ativar; administrar; fazer;
calcular; comprir; continuar;
vazar; despir-se;
concorrer
same mesmo; idêntico; igual;
parecido
de forma parecida; de forma
idêntica
mesmo; mesma coisa
sit,sat,sat sentar; sentar-se; presidir;
chocar; incubar; posar (modelo)
save salvar; poupar; economizar;
guardar; aproveitar; evitar
salvo, exceto, fora isso
salvação (no esporte etc)
say dizer; contar; recitar; pensar;
alegar; afirmar
declaração; expressão de
opinião; poder de decisão
dito, suposto, "digamos que"
scarcely dificilmente; quase que não
school escola; colégio; faculdade;
ginásio; método; cardume de
peixes
escolar
ensinar; educar; guiar; obter
bolsa de estudos; criar lagoas
(para criação de peixes)
sea mar; oceano; onda; vaga
marítimo; marinho; naval
second segundo; outro; próximo
segundo; b
momento; segundo;
instantaneamente; segundo;
apoio; suporte; ajudante
cooperar, apoiar a-; votar a
favor; ajudar, auxiliar
secret segredo; mistério; enigma;
oculto; secreto; místico
secreto; misterioso; escondido,
oculto, encoberto
see,saw,seen ver; entender;
preocupar-se; verificar;
experimentar; acompanhar;
encontrar-se; observar
sé; sede pontifical, sede
episcopal
seem parecer; parecer-se; aparentar;
aparecer
self ego; egoísmo; personalidade;
independente
o próprio, a própria
si próprio, a própria pessoa
homogêneo
senate senado; corpo legislativo
sense sentido; sentimento; razão,
consciência; bom senso, juízo ,
sensatez; lógica; compreendido,
significado; utilidade
sentir, perceber
send,sent,sent mandar; remeter;
despachar; enviar; produzir;
emitir; derramar; espalhar; dar
prazer (gíria)
service serviço; trabalho; utilidade;
cerimônia religiosa; ajuda;
invenção, oferecimento;
conjunto de louças, série
de serviço
prestar um serviço
set grupo, curso; série; conjunto;
adaptação; direção; plano;
posição; endurecimento; lugar
de filmagem
pôr, colocar; preparar; usar;
arrumar; causar; marcar; servir;
ajustar
fixo, imóvel; pronto, arrumado;
adivinho; encontro marcado
seven sete, 7
sétimo, 7
several vários, números, alguns,
separado, distinto, especial,
diferente
sharp afiado; agudo; picante; rígido;
penetrante; fogoso; astuto;
distinto; veloz; atento;
impetuoso; som agudo (música)
pontualmente; exatamente; de
forma afiado; apressadamente;
de forma falsa, acima do tom
certo
trapaceiro, impostor; sustenido,
som agudo (Música)
desafinar em meio-tom (na
música)
she fêmea; mulher
ela
fêmea, do sexo feminino
short curto; baixo; pequeno; breve;
reduzido; limitado; insuficiente;
abrupto; quebrado (sem
dinheiro)
brevemente; repentinamente;
resumidamente
curto-circuito (gíria); copo de
bebida; caranguejo (gíria);
resumo (da expressão "em
resumo")
dar troco de menos; causar
curto-circuito
shall,should (pretérito do verbo
auxiliar ”shall”) deveria, teria,
precisaria
shall
usado para exprimir futuridade
ou obrigatoriedade
show mostrar; descobrir;
testemunhar; provar;
apresentar; mostrar-se; aparecer;
ensinar; exibir
espetáculo; exibição; revista;
programa; apresentação;
impressão; descoberta; assunto;
execução
shown mostrar; descobrir;
testemunhar; provar;
apresentar; mostrar-se; aparecer;
ensinar; exibir
side lado; lateral; borda; margem;
face; laço de parentesco; declive
apoiar; ladear
lateral; secundário, colateral
sight vista; olhar; visão, aspecto;
pontaria; aparência ridícula;
ponto de vista; alcance (da vista)
avistar; perceber; alcançar com a
vista; observar; mirar; apontar;
fazer pontaria; fazer mira
silence silêncio, sossego, sussuro;
calado; mudez
silêncio !
silenciar, calar; paralisar
silver prata; cor de prata; objeto de
prata; moeda de prata, dinheiro
soante
feito de prata; prateado, coberto
de prata; de prata; claro,
claramente (voz)
pratear; cobrir de prata
similar parecido
simple simples; norma; desmontado;
tolo, ingênuo, inocente; simples
modo de andar
since desde então, do mesmo dia;
antes, anteriormente
desde
desde; visto que, por causa de,
posto que
single só, único, sozinho; solteiro,
livre; para único (quarto etc..);
de solteira; separado; encher
(união)
solteiro, desimpedido;
passagem só de ida; quarto de
solteiro; disco compacto, disco
com uma só canção; só, único
escolher, selecionar, escolher um
entresir senhor, meu senhor, mestre
six seis, 6
sexto, seis, 6
skin pele; casca; parte externa;
couro; forro
tirar a pele; descascar; remover;
ser arranhado (no joelho etc);
enganar, tapear (gíria)
sleep,slept,slept sono; sesta;
descanso
dormir; descansar; deitar (com
alguém)
slowly lentamente, vagarosamente,
em lentidão; moderadamente
small pequeno; miúdo; baixo; barato
(contrário de caro); fraco; suave;
mesquinho
em voz baixa; em pequenos
pedaços (bolos, pão, etc)
a parte estreita (das costas)
smile sorriso; riso; graça; favor
sorrir; rir; favorecer
so assim
assim; portanto; tanto; tão; de
modo que; então; suposto que
assim que
assim; algo assim; porque sim
e então, e aí
society sociedade; alta sociedade;
grupo, associação
social, da sociedade; da alta
sociedade
soldier soldado; militar; soldado
simples, guerreiro
servir o exército; fugir do
trabalho (gíria)
some algum; qualquer um; pouco;
um tanto; certo; uns; qualquer
de uma certa forma; muito
(gíria)
quanto; alguns
something algo, alguma coisa; algo
especial (gíria)
de certa forma, um tanto, algo
algo, falar algo; e mais alguma
coisa (trinta e alguma coisa
(mais de trinta) etc...)
sometimes às vezes, combinar, de
vez em quando, lentamente
somewhat um pouco, um tanto; de
certa forma, de maneira que,
algo; em alguma coisa
son filho
soon em breve; em pouco tempo; o
mais rápido; já; cedo
sort tipo, espécie; forma, maneira
classificar, ordenar; selecionar;
reparar; associar-se (com-);
combinar (para-)
soul alma, espírito, alma viva;
sentimento, coração; criatura,
habitante; canto; materialização
sound voz; ruído; som; sonda;
estreito, canal; bexiga natatória
ouvir; escutar; parecer; criar a
impressão; emitir ruído, tocar,
fazer soar ; verificar; medir
profundidade
são, sadio; sólido; inteiro;
profundo; seguro; certo; forte;
legítimo; completo; sonoro;
solvável; leal; honesto
south sul
do sul
para o sul, em direção ao sul
sovereign soberano (moeda de
ouro); rainha, rei, governador,
senhor, chefe
soberano, dominador, poderoso;
excelente, ótimo
speak,spoke,spoken falar; dizer;
contar; expressar; discursar;
lembrar a-; afirmar
spoke
raio (de roda); travão (de roda);
degrau (de escada)
speed velocidade; rapidez;
estimulante; acelerador (no
carro)
apressar-se; mover com
velocidade; dirigir muito
rápido; ser feliz; ser bem
sucedido; adiantar; aviar;
despachar
spirit alma, espírito; criatura,
habitante; fantasma, demônio ;
coragem, força, vigor
estimular, dar energia, reforçar
stand pôr de pé; suster; sustentar;
colocar; aguentar; honrar;
manter-se; permanecer
de pé; estrado; proteção; posto
de taxi
start começo; pulo, sobressalto;
arranque; impulso
começar, iniciar; abrir; sair a
caminho; arrancar; partir; fazer
funcionar, ligar
state situação; estado; bagunça
declarar; expressar; determinar
estatal; público; de cerimônia
still ainda; mais; apesar; sempre
tranqüilo; silencioso; imóvel
fotografia; tranquilidade;
alambique
tranquilizar; calar
stone pedra; pedra preciosa;
testículo; medida de massa
de pedra, pedregoso
totalmente
apedrejar, endurecer, enrijecer;
descaroçar
stop parar; estacionar; suspender;
atrasar; barrar; interromper;
hospedar-se
parada; atraso; pausa;
interrupção; repressão; ponto
story história; relatório; descrição;
ficção; reportagem
strange estranho; esquésito,
esquisito
street rua; estrada
strength força; resistência, dureza;
lápide; monumento
strong forte; poderoso; vigoroso;
musculoso; indigesto
com força, fortemente
strike,struck,striken golpear; ferir;
bater; surpreender; descobrir
struck
batido, agarrado
subject assunto; sujeito, pessoa;
matéria, profissão, ramo
sujeitar; revelar; passar
sujeito, subalterno; tendente
success sucesso; pessoa bem
sucedida
such semelhante; igual
como; do mesmo modo
tal; aquele (a), aqueles (as)
sudden repentino, imprevisto
subitamente
suffer sofrer; ter prejuízo; tolerar
sufficient suficiente
sun sol
expor ao sol; insolar; tomar
banho de sol; brilhar;
esquentar-se no sol
superior superior, chefe
superior; altivo
suppose supor, crer
sure claro; óbvio; certo; verificado
obviamente; claramente
sweet doce; açucarado; melodioso;
meigo; carinhoso
bala, doce; compota
com doçura
swift rápido, ligeiro; imediato
tipo de pássaro
Swift
Swift (Jonathan, escritor inglês,
autor de "As Viagens de
Guliver")
sword espada
system sistema; corpo; programa
table mesa; refeição; tabuleiro
pôr sobre a mesa (proposta etc)
take,took,taken pegar; tirar; tomar;
segurar; agarrar; receber;
capturar; aprisionar; aceitar;
fotografar; empregar; adotar;
entender; guiar; conseguir
entrada; recepção; introdução
talk conversar; contar
conversa; palestra
tear,tore,torn lágrima; rasgar,
romper; festança
chorar, lacrimejar; rasgar, rachar
ten dez, 10
carta que vale dez pontos; nota
de dez dólares; décimo
than o mesmo que
que, do que
that esse (a), aquele (a) , o, a
tão; até que
que, quem, o qual
que, para que, afim de que
the o, a, os, as
tanto , quanto
their deles, delas (antes da palavra)
them os, as, eles, elas, lhes
themselves eles mesmos, a si
mesmos
then então, na mesma hora
portanto, por isso
então, e depois
there lá, ali, para lá
tem
não faz mal; veja!(consolo)
therefore então
these estes, aqueles
estes, estas
they eles, elas
thing coisa, objeto; ação; assunto;
criatura; idéia
think,thought,thought pensar;
acreditar
pensamento, reflexão
third terceiro
terço
thirty trinta, 30
this este, esta
isso, isto
tanto, até que
those aqueles
aqueles, aquelas
though apesar
de qualquer forma
thousand mil 1000

three três, 3
três

throne trono

through através; de lado a lado
através, por; dentro
direto

thus assim, dessa forma, deste modo

till até que
até
cultivar, trabalhar (a terra)
gaveta

time tempo; época; hora; ritmo
de tempo
determinar o tempo

tin lata, dinheiro, estanho
feito de lata, de lata
enlatar, conservar em latas;
cobrir com estanho

title título; rótulo; denominação
honorífica; atributo; direito;
posse; vitória num campeonato
entitular, rotular

to para a situação anterior; de acordo
com; em homenagem a
para, a; em contraposição a; com
o intuito de

together juntos, juntamente, em
companhia, ao mesmo tempo

tell,told,told contar; saber; perceber;
descobrir; ordenar

too demais; também

toward para; em direção a; voltado
para

town de cidade, urbano, municipal

tree árvore; trave; arbusto

troop tropa; bando, companhia
marchar em grupo

trouble confusão, preocupação,
inquietação
aborrecer, preocupar; inquietar;
irritar

true verdade
certo; verdadeiro; exato, fiel
de verdade; exato
adequar exatamente, adequar
com precisão

truth verdade, honestidade

try tentar; testar; julgar; adotar
tentativa, teste

"""

blocos = texto.strip().split('\n\n')

dados = []
for bloco in blocos:
    # Removendo possíveis espaços em branco extras e dividindo por quebra de linha
    linhas = [linha.strip() for linha in bloco.split('\n') if linha.strip()]
    # Verificando se existe pelo menos uma linha no bloco processado
    if linhas:
        # A primeira linha contém a palavra em inglês seguida da descrição na mesma linha
        # ou em linhas subsequentes
        partes = linhas[0].split(maxsplit=1)  # Divide a primeira linha em no máximo duas partes
        palavra = partes[0] if partes else ""
        # A descrição pode começar na mesma linha da palavra ou nas linhas seguintes
        descricao = partes[1] if len(partes) > 1 else ""
        descricao += " ".join(linhas[1:])  # Adiciona o restante das linhas à descrição
        if palavra:  # Adiciona ao resultado se uma palavra foi encontrada
            dados.append({"Palavra": palavra, "Descrição": descricao.strip()})

# Salvar os dados em um arquivo JSON
with open('dados_dicio.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)

print("Dados salvos em 'dados_dicio.json'.")