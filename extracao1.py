import re
import json
import pdfplumber  # Você precisa instalar a biblioteca pdfplumber

# Expressão regular para capturar as partes
regex = r"^(\w+)\s+(\S+)\s+(.+)$"

texto_completo = '''
a â um, uma
able eibâl capaz
about âbaut sobre, quase
above âbâv acima
act ékt ato, agir
add éd adicionar
afraid âfreid com
-medo
after éftâr após
again âghein de
-novo
against âghenst contra
age eij idade
ago âgou atrás
agree âgrii concordar
air ér ar
all ól todo
allow âlau permitir
also ólsou também
always óluêz sempre
am ém sou, estou
among âmâng entre
an én um, uma
and énd
e
anger éngâr raiva
animal énâmâl animal
answer énsâr resposta
any éni qualquer
appear âpiir aparecer
apple épâl maçã
are ar são, estão
area ériiâ área
arm arm braço
arrange âreindj arranjar
arrive âraiv chegar
art art arte
as és como, enquanto
ask ésk pedir, perguntar
at ét em
atom étâm átomo
baby beibi bebê
back bék atrás, costas
bad béd mal
ball ból bola
band bénd banda
bank bénk banco
bar bar bar, barra
base beis base
basic beisêk básico
bat bét morcego, bastão
be bii ser, estar
bear bér urso, carregar
beat biit bater
beauty biutti beleza
bed bed cama
been bên sido, estado
before bêfór antes
began bêgén começado
begin bêghên começar
behind bêrraind atrás
believe bêliiv acreditar
bell beól sino
best best melhor
better bettâr melhor
between bituiin entre
big bêg grande
bird bârd pássaro
bit bêt pouco, broca
black blék negro
block blak bloco
blood blâd sangue
blow blou assoprar
blue bluu azul
board bórd quadro
boat bout barco
body baddi corpo
bone boun osso
book bôk livro
born bórn nascido
both bouth ambos
bottom battâm baixo
bought bót comprado
box baks caixa
boy bói garoto
branch brénch galho
bread bréd pão
break breik quebrar
bright brait claro
bring brêng trazer
broad bród amplo
broke brouk quebrado
brother brâdhâr irmão
brought brót trazido
brown braun marrom
build bêld construir
burn bârn queimar
busy bêzi ocupado
but bât mas
buy bai comprar
by bai por, em
call cól chamar
came keim chegado
camp kémp campo
can kén pode, lata
capital képêtâl capital
captain képtân capitão
car car carro
card card cartão
care kér cuidado
carry kéri carregar
case keis caso, embalagem
cat két gato
catch kétch pegar
caught cót pego
cause cóz causa
cell ceól cela, célula
cent cent centavo
center centâr centro
century centri século
certain sârtân certo
chair tchér cadeira
chance tchéns chance, acaso
change tcheinj mudar
character kérêktâr caráter, personagem
charge chardj carga, cobrança
chart tchart gráfico
check tchek cheque, checagem
chick tchêk pintinho
chief chiif chefe
child tchaild criança
children tchêldrân crianças
choose tchuuz escolher
chord córd acorde
circle sârkâl círculo
city cêtti cidade
claim cleim clamar
class clés classe
clean cliin limpo
clear cliir claro
climb claim escalar
clock clak relógio
close clous fechar
clothe cloudh vestir
cloud claud nuvem
coast coust costa, litoral
coat cout casaco
cold could frio
collect câlect recolher, pagar
colony calâni colonia
color câlâr cor, colorir
column calâm coluna
come câm vir
common camân comum
company câmpâni companhia, empresa
compare câmpér comparar
complete câmpliit completo
condition cândêshân condição
connect cânect conectar
consider cânsêdâr considerar
consonant cansânânt consoante
contain cântein conter
continent cantânânt continente
continue cântêniu continuar
control cântroul controle
cook côk cozinhar
cool cuul frio
copy capi copiar
corn córn milho
corner córnâr esquina
correct cârekt correto
cost cóst custo
cotton catân algodão
could côd poderia
count caunt contar, contagem, conde
country cântri país
course córs curso
cover câvâr cobrir
cow cau vaca
crease criis ruga
create crieit criar
crop crap colheita
cross crós cruz, cruzar
crowd craud multidão
cry crai choro, chorar
current cârânt atual
cut cât cortar
dad déd papai
dance déns dança
danger deindjâr perigo
dark dark escuro
day dei dia
dead ded morto
deal diil negócio
dear diir querido
death deth morte
decide dêsaid decidir
decimal dêsêmâl decimal
deep diip profundo
degree dêgrii grau
depend dêpend depender
describe dêcraib descrever
desert dêzârt deserto
design dêzain desenho
dessert dêssârt sobremesa
determine dêtârmân determinar
develop dêvelâp desenvolver
dictionary dêkshânâri dicionário
did dêd fez, mesmo
die dai morrer
differ dêfâr diferir
difficult dêfêcâlt difícil
direct dârekt direto
discuss dêscâs discutir
distant dêstânt distante
divide dêvaid dividir
division dêvêzhân divisão
do duu fazer, mesmo
doctor dactâr doutor
does dâz faz, mesmo
dog dóg cachorro
dollar dalâr dólar
done dân feito
don't dount não
door dór porta
double dâbâl dobro
down daun baixo
draw dró arrastar, empate
dream driim sonho
dress dres vestido
drink drênk bebida
drive draiv direção, dirigir
drop drap gota
dry drai seco
duck dâk pato, mergulhar
during duurêng durante
each iich cada
ear iir orelha, espiga
early ârli cedo
earth ârth terra
ease iiz facilitar
east iist leste
eat iit comer
edge ej canto
effect êfect efeito
egg eg ovo
eight eit oito
either aidhâr um, ou outro, também
electric êlektrêk elétrico
element elêmânt elemento
else els outro
end ênd fim, finalizar
enemy enâmi inimigo
energy enârji energia
engine enjân motor
enough inâf bastante
enter enttâr entrar
equal iiquâl igual
equate iiqueit equacionar
especially êspeshâli especialmente
even iivân mesmo
evening iivnêng noite
event ivent evento
ever evâr sempre, já
every evri cada
exact igzéct exato
example igzémpâl exemplo
except êkscept exceto
excite iksait instigar
exercise eksârsaiz exercício
expect ikspekt esperar
experience êkspiiriâns experiência
experiment eksperâmânt experimento
eye ai olho
face feis rosto
fact fékt fato
fair fér feira, claro
fall fól cair, queda, outono
family fémâli família
famous feimâs famoso
far far longe
farm farm fazenda
fast fést rápido
fat fét gordo
father fódhâr pai
favor feivâr favor, favorecer
fear fiir medo, temer
feed fiid alimentar
feel fiiól sentir, sentimendo
feet fiit pés
fell fel caido
felt feólt sentido
few fiu alguns
field fiild campo
fig fêg figo
fight fait luta
figure fêghiâr figura, imaginar
fill fêl encher
final fainâl final
find faind encontrar
fine fain bom, excelente
finger fêngâr dedo
finish fênish fim, finalizar
fire fair fogo, incêndio, despedir
first fârst primeiro
fish fêsh peixe, pescar
fit fêt ajustado
five faiv cinco
flat flét achatado, plano
floor flór chão, derrotar
flow flou correr, corrente
flower flauâr flor
fly flai voar, mosca
follow falou seguir
food fuud comida
foot fuut pé
for fór por, para
force fórs força, forçar
forest fórâst floresta
form fórm forma, formulário
forward fóruârd adiante, passar adiante
found faund encontrado, fundar
four fór quatro
fraction frécshân fração
free frii livre, grátis
fresh fresh fresco
friend frend amigo
from frâm de
front frânt frente
fruit fruut fruta
full fôl cheio
fun fân alegria
game gheim jogo
garden gardân jardim
gas ghés gás, gasolina
gather ghédhâr juntar
gave gheiv dado
general jenral general, geral
gentle jentâl gentil
get ghét ficar
girl gârl garota
give ghêv dar
glad gléd contente
glass glés vidro
go gôu ir
gold gould ouro
gone gón ido
good gôd bom
got gat ficado
govern gâvârn governar
grand grénd grandioso
grass grés grama
gray grei cinza
great greit ótimo, excelente, grande
green griin verde
grew gruu crescido
ground graund terra, amolado
group grup grupo
grow grou crescer
guess ghes adivinhar
guide gaid guia, guiar
gun gân arma
had rréd tinha
hair rrér cabelo
half rréf metade
hand rrénd mão
happen rrépân acontecer
happy rrépi feliz
hard rrard duro
has rrés tem
hat rrét chapéu
have rrév ter
he rrii ele
head rred cabeça
hear rriir ouvir
heard rrârd ouvido
heart rrórt coração
heat rriit calor
heavy rrevi pesado
held rreld guardado
help rrêlp ajudar
her rrâr dela
here rriir aqui
high rrai alto
hill rrêl colina
him rrêm dele
his rrês seu
history rrêstâri história
hit rrêt acertar
hold rrould guardar
hole rroul buraco
home rroum casa
hope rroup esperança
horse rrórs cavalo
hot rrat quente
hour aur hora
house rraus casa
how rráu como, quão
huge rriudj grande, enorme
human rriumân humano
hundred rrândrâd cem
hunt rrânt caçar
hurry rrâri pressa
I ai eu
ice ais gelo
idea aidiia idéia
if êf se
imagine êmédjân imaginar
in ên em, dentro
inch êntch polegada
include ênclud incluir
indicate êndêkeit indicar
industry êndâstri indústria
insect ênsect inseto
instant ênstânt instante
instrument ênstrâmânt instrumento
interest êntrâst interesse, juros
invent ênvent inventar
iron airn ferro
is ês é
island ailând ilha
it êt este
job jáb trabalho, jó
join join juntar
joy jói alegria
jump jâmp pular
just jâst justo, só
keep kiip guardar
kept kept guardado
key kii chave
kill kêl matar
kind kaind bom, tipo
king kêng rei
knew nuu sabido
know nou saber
lady leidi dama
lake leik lago
land lénd terra
language lénguêj língua
large larj grande
last lést último, durar
late leit tarde
laugh léf rir
law ló lei
lay lei deitar, amador
lead liid levar, chumbo
learn lârn aprender
least liist menos
leave liiv deixar
led led levado
left left esquerda, deixado
leg leg perna
length lenth comprimento
less les menos
let let deixar
letter lettâr letra, carta
level levâl nível
lie lai deitar, mentir
life laif vida
lift lêft levantar
light lait leve, luz
like laik como, gostar
line lain linha, fila
liquid lêquâd líquido
list lêst lista
listen lêssân ouvir
little lêttâl pequeno, pouco
live lêv, laiv viver, vivo
locate loukeit localizar
log lóg lenha, diário
lone loun só
long lóng longo
look lôk olhar
lost lóst perdido
lot lót muito, lote
loud laud alto(som)
love lâv amor, amar
low lou baixo
machine mâshiin máquina
made meid feito
magnet mégnât imã
main mein principal
major meidjâr maior, major
make meik fazer
man mén homem
many méni muitos
map mép mapa
mark mark marcar
market markât mercado
mass més massa, missa
master méstâr mestre
match métch competição, fósforo
material mâtiiriâl material
matter méttâr matéria, importar-se
may mei maio, pode
me mii me, eu
mean miin meio, significar
meant ment significado
measure mejâr medida
meat miit carne
meet miit encontrar
melody melâdi melodia
men mên homens
metal mettâl metal
method méthâd método
middle mêdâl meio
might mait poder, poderia
mile mail milha
milk mêlk leite
million mêliân milhão
mind maind mente, importar-se
mine main meu, mina
minute mênât minuto
miss mês sentir, senhorita
mix mêks mistura
modern madârn moderno
molecule malêkiul molécula
moment moumânt momento
money mâni dinheiro
month mânt mês
moon muun lua
more mór mais
morning mórnên manhã
most moust mais, maior
mother mâdhâr mãe
motion moushân movimento
mount maunt monte, montar
mountain mauntân montanha
mouth mauth boca
move muuv movimento
much mâtch muito
multiply mâltâplai multiplicar
music miuzêk música
must mâst dever
my mai meu
name neim nome
nation neishân nação
natural nétchârâl natural
nature neitchâr natureza
near niir perto
necessary nesâséri necessário
neck nek pescoço
need niid precisar
neighbor neibâr vizinho
never nevâr nunca
new nuu novo
next next próximo
night nait noite
nine nain nove
no nou não
noise nóiz barulho
noon nuun meio-dia
nor nór nem
north nórth norte
nose nouz nariz
note nout anotar
nothing nâthêng nada
notice nottâs aviso
noun naun substantivo
now nau agora
number nâmbâr número
numeral nuumârâl numeral
object âbjêkt objeto
observe âbzârv observar
occur âcâr ocorrer
ocean oushân oceano
of âv de
off óf por, desligado
offer afêr oferecer
office afâs escritório, função
often ófân muitas-vezes
oh ou ó
oil oil óleo, petróleo
old ould velho
on ón em
once uâns uma-vez
one uân um
only ounli somente
open oupân aberto
operate apâreit operar
opposite apâzât oposto
or ór ou
order órdâr ordem, pedido
organ órgân órgão
original ârêdjânâl original
other âdhâr outro
our ar nosso
out aut fora
over ouvâr sobre, acima-de
own oun próprio
oxygen aksêdjân oxigênio
page peij página
paint peint pintar
pair pér par
paper peipâr papel
paragraph pérâgréf parágrafo
parent pérânt pais
part part parte
particular partêkiâlar especial
party party partido, festa
pass pés passar
past pést passado
path péth caminho
pattern péttârn padrão
pay pei pagar
people piipâl pessoas, povo
perhaps pârhépps talvez
period pêriiâd período
person pârsân pessoa
phrase freiz frase
pick pêk escolher, apanhar
picture pêktchâr foto, filme
piece piis peça, pedaço
pitch pêtch piche, arremeço
place pleis lugar
plain plein plano, simples
plan plén plano
plane plein avião
planet plénât planeta
plant plént planta, fábrica
play plei peça, tocar
please pliiz por-favor, agradar
plural plôrâl plural
poem pouêm poema
point point ponto
poor pôr pobre
populate papiâleit povoar
port pórt porto
pose pouz posição
position pâzêshãn posição
possible pasâbâl possível
post poast pós, posto
pound paund libra
power pauâr poder, força
practice précttâs prática
prepare prêpér preparar
present prezânt presente
press pres pressão, imprensa
pretty prêti belo, muito
print prênt imprimir
probable prabâbâl provável
problem prablâm problema
process prouces processo
produce prâdus produção
product pradâkt produto
proper prapâr próprio
property prapâtti propriedade
protect prâtect proteger
prove pruuv provar
provide prâvaid fornecer
pull pôl puxar
push pôsh empurrar, iniciativa
put pôt por
quart quórt quarto(medida)
question quéschân questão, pergunta
quick quêk rápido
quiet quait quieto
quite quait muito
quotient quoshânt quociente
race reis raça, corrida
radio reidiiou rádio
rail reil grade, trilho
rain rein chuva
raise reiz levantar
ran rén corrido
range reindj alcance, pastagem
rather raadhâr de-preferência
reach riitch alcançar
read riid ler, lido
ready riidi pronto
real riil real
reason riizân razão
receive riciiv receber
record recârd recorde, gravar, registro
red red vermelho
region riijân região
remember rimembâr lembrar
repeat rêpiit repetir
reply rêplai resposta
represent reprêzent representar
require rêquair exigir
rest rest resto, descanso
result rêzâlt resultado
rich rêtch rico
ride raid passeio
right rait direito
ring rêng anel, tocar
rise raiz levantar
river rêvâr rio
road roud estrada
rock rak roque, rocha
roll rôl giro, lista
room ruum cômodo, quarto
root ruut raiz
rope roup corda
rose rouz rosa, levantado
round raund redondo, rodada
row rou remar, fila
rub râb esfregar
rule ruul régua, regra
run rân correr
safe seif seguro, cofre
said séd disse
sail seil vela(navio)
salt sólt sal
same seim mesmo
sand sénd areia
sat sét sentado
save seiv salvar
saw só viu, serra
say sei dizer
scale skeil escada, escala, escama
school skool escola
science sains ciência
score scór placar, duas-dezenas
sea sii mar
search sârtch buscar
season seezân estação
seat siit assento
second secând segundo
section sekshân seção
see sii ver
seed siid semente
seem siim parecer
segment segmânt segmento
select sêlect selecionar
self self próprio, ego
sell sel vender
send send enviar
sense sens sentido
sent sent enviado
sentence sêntâns sentença
separate sepârât separado
serve sârv servir
set sêt conjunto, fixar
settle settâl estabelecer
seven sevân sete
several sevrâl vários
shall shél vai
shape sheip forma
share shér parte
sharp sharp agudo, sustenido
she shii ela
sheet shiit folha, lençol
shell shel concha
shine shain brilhar
ship shêp navio, embarcar
shoe shuu sapato
shop shap loja
shore shór praia
short shórt curto
should shôd deveria
shoulder shouldâr ombro
shout shaut gritar
show shou mostrar
side said lado
sight sait visão
sign sain sinal
silent sailânt silencio
silver sêlvãr prata
similar sêmâlãr semelhante
simple sêmpâl simples
since sêns desde
sing sêng cantar
single sêngâl só, solteiro
sister sêstâr irmã
sit sêt sentar
six sêks seis
size saiz tamanho
skill skêl habilidade
skin skên pele
sky skai céu
slave sleiv escravo
sleep sliip dormir
slip slêp escorregar
slow slou devagar
small smól pequeno
smell smel cheiro
smile smail sorriso
snow snou neve
so sôu assim, tão
soft saft macio
soil sóil solo
soldier souldjãr soldado
solution sâlushân solução
solve soulv resolver
some sâm algum
son sân filho
song sóng canção
soon suun logo
sound saund som
south sauth sul
space speis espaço
speak spiik falar
special speshâl especial
speech spiitch discurso
speed spiid velocidade
spell spêl soletrar, encanto
spend spend gastar
spoke spouk falado, raio
spot spat ponto
spread spred espalhar
spring sprêng primavera, mola
square squér quadrado, praça
stand sténd permanecer, de-pé, banca
star star estrela
start start começar
state steit estado
station steishân estação
stay stei ficar
stead sted local
steam stiim vapor
steel stiil aço
step step passo
stick stêk vareta, fincar
still stêl até, calmo
stone stoun pedra
stood stud permanecido
stop stap parar
store stór armazém
story stóri estória, andar(prédio)
straight streit reto
strange streindj estranho
stream striim corrente
street striit rua
stretch stretch alcance
string strêng corda
strong stróng forte
student stuudânt estudante
study stâdi estudo
subject sâbjêkt sujeito, assunto
substance sâbstâns substância
subtract sâbtréct subtrair
success sâkses sucesso
such sâtch tal
sudden sâdân imprevisto
suffix sâfêks sufixo
sugar shuugâr açúcar
suggest sâgjest sugerir
suit suut terno
summer sâmâr verão
sun sân sol
supply sâplai suprir
support sâpórt apoiar
sure shôr certo
surface sârfâs superficie
surprise sârpraiz surpresa
swim suêm nadar
syllable sêlâbâl sílaba
symbol sêmbâl símbol
system sêstâm sistema
table teibâl mesa, tabela
tail teil rabo
take teik pegar
talk tók conversar
tall tól alto(pessoa)
teach tiitch ensinar
team tiim grupo
teeth tiith dentes
tell têl contar
temperature temprâchâr temperatura
ten ten dez
term târm termo, período
test test teste
than dhén que
thank thénk agradecer
that dhét que, aquele
the dhâ o, a, os, as
their thér seus
them dhêm deles
then dhên então
there thér lá
these dhiiz estes
they dhei eles
thick thêk grosso
thin thên fino, magro
thing thêng coisa
think thênk pensar
third thârd terceiro
this dhês este
those dhouz aqueles
though thou apesar-de
thought thót pensamento, pensado
thousand thauzând mil
three thrii três
through thruu através-de
throw throu arremessar
thus dhâs assim
tie tai amarrar
time taim tempo, hora
tiny taini minúsculo
tire tair pneu, cansar
to tuu para
together tâghedhâr juntos
told tould contado
tone toun tom
too tuu também
took tôk pego
tool tuul ferramenta
top tap topo, principal
total toutãl total
touch tâtch tocar
toward tuuard para
town taun municipal
track trék trilha
trade treid comércio
train trêin trem, treinar
travel trévâl viajar
tree trii árvore
triangle traiéngâl triângulo
trip trêp viajar, passeio
trouble trâbâl preocupação
truck trâk caminhão
true truu VERDADEIRO
try trai tentar
tube tuub tubo, tv
turn târn tornar, vez
twenty tuenti vinte
two tuu dois, duas
type taip tipo, datilografar
under ândâr sob
unit iunât unidade
until ântêl até
up âp para-cima
us âs nos
use iuz usar
usual iuzhuâl usual, comum
valley véli vale
value véliu valor
vary véri variar
verb vârb verbo
very véri muito, absoluto
view viu vista
village vêlâj vila
visit vêzât visita
voice vois voz
vowel vaul vogal
wait ueit esperar
walk uók andar
wall uól parede
want uânt querer
war uar guerra
warm uórm quente
was uós era, estava
wash uósh lavar
watch uótch assistir, relógio
water uóttâr água
wave ueiv onda
way uei caminho, jeito
we uii nós
wear uér usar
weather uedhâr tempo
week uiik semana
weight ueit peso
well uel bem, poço
went uent foi
were uâr eram, esavam
west uest oeste
what uót o-que
wheel uiil roda
when uen quando
where uér onde
whether uedhâr se
which uêtch qual
while uail enquanto
white uait branco
who rruu que
whole rroul inteiro
whose rruuz cujo
why uai por-que
wide uaid amplo
wife uaif esposa
wild uaild selvagem
will uêl vai, vontade
win uên ganhar
wind uênd vento
window uêndou janela
wing uêng asa
winter uênttâr inverno
wire uair arame
wish uêsh desejo
with uêdh com
woman uômân mulher
women uêmân mulheres
wonder uândâr admirar
won't uount não-vai
wood uôd madeira
word uâd palavra
work uârk trabalho
world uârld mundo
would uôd deveria
write rait escrever
written rêtân escrito
wrong róng errado
wrote rout escrito
yard yard jarda, quintal
year yiir ano
yellow yelou amarelo
yes yes sim
yet yet ainda, já
you yuu você
young yâng jovem
your yór seu
'''

# Encontrar todas as correspondências da regex
resultados = re.findall(regex, texto_completo, re.MULTILINE)

# Convertendo os resultados para um formato JSON
dados_json = [{"Palavra": res[0], "Pronúncia": res[1], "Tradução": res[2]} for res in resultados]

# Salvar os dados em um arquivo JSON
with open('dados.json', 'w', encoding='utf-8') as f:
    json.dump(dados_json, f, ensure_ascii=False, indent=4)

print("Dados salvos em 'dados.json'.")
