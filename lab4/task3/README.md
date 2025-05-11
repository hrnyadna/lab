## Лабораторная работа 4, задание 3: Трансляция

## Цель
Получить аминокислотные (белковые) последовательности, которые кодируются в заданных нуклеотидных цепочках, на основе анализа кодирующих областей в файле GenBank.
## Задачи
1) Считать файл sequences.gb, содержащий последовательности двух видов в формате GenBank.

2) Найти все кодирующие области (CDS) в каждой записи.

3)  Для каждой кодирующей области:

- Определить её координаты (начало, конец, направление).

- Выполнить трансляцию нуклеотидной последовательности в аминокислотную.

4) Вывести на экран:

- идентификатор и описание последовательности,

- положение кодирующей области,

- соответствующую белковую цепочку

## Что делала
Открываем файл и читаем каждую запись отдельно - для сапсана и яблони. Для каждой записи он выводит ее ID и описание, чтобы было понятно, с какой последовательностью мы работаем.
Код проходит по всем особенностям (features) этой записи и ищет именно кодирующие последовательности (те, у которых тип "CDS"). Для каждой найденной CDS он определяет ее точное расположение в ДНК - начало и конец, а также на какой цепи она находится (прямая или обратная). Если в аннотациях уже есть готовая белковая последовательность (translation), код просто берет ее. Если нет - он сам извлекает ДНК-последовательность этого гена и переводит ее в белок, используя стандартную таблицу генетического кода. Полученную белковую последовательность код разбивает на строки по 60 символов, чтобы было удобно читать. Между разными генами он ставит разделитель из символов "=", чтобы визуально отделять результаты. 

## Результат
В итоге мы получаем полную информацию о том, где именно в ДНК расположен каждый ген и какой белок он кодирует, причем все гены обрабатываются автоматически один за другим. Вот так все выглядит:
MN168306.1: Falco peregrinus aquaporin 14 (Aqp14) gene, complete cds

Coding sequence location = [1:780](+)
Translation =
MAIREELRSWCFWQGVLVEAVATLIFVGVVLGASVDPRPLAPALAGGLVAGALVCTLRAP
QANPALTLALLCTRKLSALRGAAGLLAQCTGAVLASAIARLALPDDTSLVTRVSAAGTAG
QALAWETFATFQLALAAFATTDQVAPQGGLALGSAVAALALAAGPFSGGSMNPARSLGPA
IVTGIWDDHWVSWLGPVLCAVLAGLSYEFIFAPGASREKLGACLACRDVALVETTSPSPS
SASTRGHPAPPAERDQGTA

================================================================================

DQ165481.1: Falco peregrinus R2 cytochrome oxidase subunit II (COXII) gene, complete cds; mitochondrial

Coding sequence location = [1:684](+)
Translation =
MANQSQLGFQDASSPIMEELVEFHDHALMVALAICSLVLYLLTLMLAEKLSSNTVDAQEV
ELIWTILPAIVLILLALPSLQILYMMDEIDEPDLTLKAIGHQWYWAYEYTDFKDLTFDSY
MIPTTELPSGHFRLLEVDHRIVIPMESPIRIIITANDVLHSWAVPSLGVKTDAIPGRLNQ
TSFITTRPGVFYGQCSEICGANHSYMPIVVESTPLTHFEHWSTLLSS

================================================================================

DQ165480.1: Falco peregrinus OK67 cytochrome oxidase subunit II (COXII) gene, complete cds; mitochondrial

Coding sequence location = [1:684](+)
Translation =
MANQSQLGFQDASSPIMEELVEFHDHALMVALAICSLVLYLLTLMLAEKLSSNTVDAQEV
ELIWTILPAIVLILLALPSLQILYMMDEIDEPDLTLKAIGHQWYWAYEYTDFKDLTFDSY
MIPTTELPSGHFRLLEVDHRIVIPMESPIRIIITANDVLHSWAVPSLGVKTDAIPGRLNQ
TSFITTRPGVFYGQCSEICGANHSYMPIVVESTPLTHFEHWSTLLSS

================================================================================

U83307.1: Falco peregrinus cytochrome b (cytb) gene, mitochondrial gene encoding mitochondrial protein, complete cds

Coding sequence location = [1:1143](+)
Translation =
MAPNIRKSHPLVKMINNSLIDLPTPPNISIWWNFGSLLGICLATQILTGLLLAMHYTADT
TLAFSSVAHTCRNVQYGWLIRNLHANGASLFFICIYMHIGRGIYYGSYLYKETWNTGIIL
LLTLMATAFVGYVLPWGQMSFWGATVITNLFSAIPYIGQTLVEWAWGGFSVDNPTLTRFF
ALHFLLPFLIAGLTLIHLTFLHESGSNNPLGITSNCDKIPFHPYYSLKDILGFMLMYLPL
MTLALFTPNLLGDPENFTPANPLVTPPHIKPEWYFLFAYAILRSIPNKLGGVLALAASVL
ILFLSPLLHKSKQRTMTFRPLSQSLFWLLVTNLLILTWVGSQPVEHPFIIIGQLASLSYF
TTLLILLPLTGALENKILNY

================================================================================

KR269733.1: Falco peregrinus clone B opioid receptor Kappa 1 isoform B (OPRK1) mRNA, complete cds, alternatively spliced

Coding sequence location = [7:648](+)
Translation =
MDAPVQIFREETESTCSPVPCRAPSTSGSWLLGWVDYDSNATGAFGGTQHNHTSISPAIP
IIITAVYSVVFVVGLVGNSLVMFVIIRYTKMKTATNIYIFNLAMADALVTTTMPFQSTEY
LMNSWPFGDVLCKIVISIDYYNMFTSIFTLTMMSVDRYIAVCHPVKALDFRTPLKAKIIN
ICIWLLSSSVGISAIVLGGTKVREAISENLKAW

================================================================================

KP234026.1: Malus domestica cultivar Malus domestica cv. Fuji phi class glutathione S-transferase (GSTF3) mRNA, complete cds

Coding sequence location = [50:691](+)
Translation =
MAAIKVHGNVISTAAMRVFATLYEKDIEFELVPIDMRAGEHKKEPFISLNPFGQVPAFED
GDLKLFESRAITQYIAHEYADKGTPLVIRDSKKMAIISLWSEVEAQKFDPAATKLTYELA
IKPMFKMTTDAAVVEENEAKLAVVLDVYETRLAQSKYLAGESFTLADLHHLPTIHYLMGT
QSKKLFESRPHVLAWVVDITARPAWNKVVAQQK

================================================================================

L31347.1: Malus domestica 1-aminocyclopropane-1-carboxylic acid synthase (ACC) mRNA, complete cds

Coding sequence location = [100:1521](+)
Translation =
MRMLSRNATFNSHGQDSSYFLGWQEYEKNPYHEVHNTNGIIQMGLAENQLCFDLLESWLA
KNPEAAAFKKNGESIFAELALFQDYHGLPAFKKAMVDFMAEIRGNKVTFDPNHLVLTAGA
TSANETFIFCLADPGEAVLIPTPYYPGFDRDLKWRTGVEIVPIHCTSSNGFQITETALEE
AYQEAEKRNLRVKGVLVTNPSNPLGTTMTRNELYLLLSFVEDKGIHLISDEIYSGTAFSS
PSFISVMEVLKDRNCDENSEVWQRVHVVYSLSKDLGLPGFRVGAIYSNDDMVVAAATKMS
SFGLVSSQTQHLLSAMLSDKKLTKNYIAENHKRLKQRQKKLVSGLQKSGISCLNGNAGLF
CWVDMRHLLRSNTFEAEMELWKKIVYEVHLNISPGSSCHCTEPGWFRVCFANLPERTLDL
AMQRLKAFVGEYYNVPEVNGGSQSSHLSHSRRQSLTKWVSRLSFDDRGPIPGR

================================================================================

AB032247.1: Malus domestica Sh mRNA for Sh-RNase, complete cds

Coding sequence location = [1:681](+)
Translation =
MGTGMIYMVMMVFSLILLILPSSTVGFDYYQFTQQYQPAVCNSNPTPCKDPTDKLFTVHG
LWPSNSNGNDPKYCNAQQYQTMKILEPQLVIIWPNVLNRNDHEGFWRKQWEKHGSCASSP
IQNQKHYFDTVIKMYTTQKQNISEILSKANIKPGRKNRTLVDIENAIRNVINNMTPQFKC
QKNTRTSLTELVEVGLCSDSNLTQFINCPRPFPRGSRYFCPTNIQY

================================================================================

AB032246.1: Malus domestica Sd mRNA for Sd-RNase, complete cds

Coding sequence location = [67:753](+)
Translation =
MGITGMIYMVTIVFSLIVLLLSSSAARYDYFQFTQQYQLAACNSKPIPCKDPPDKLFTVH
GLWPSDSNGHDPVNCSKSTVDAQKLGNLTTQLEIIWPNVYNRTDHISFWDKQWNKHGTCG
HPTIMNDIHYFQTVIKMYITQKQNVSKILSRAKIEPEGKPRKQVDIVNAIRKGTNDKEPK
LKCQKNNQVTELVEVTLCSNRNLTGFINCPRHIPNGSRYSCPTKNILY

================================================================================

D87670.1: Malus domestica DNA for polyphenol oxidase, complete cds

Coding sequence location = [1:1782](+)
Translation =
MTSLSPPVVTTPTVPNPDTKPLSPFSQNNSQVSLLTKPKRSFGRKVSCKDTNNDEIDQAQ
SKLERRNVLLGLGGLYGVGGMDTDPRGWGKAIAPPDVSKCGPADLPQGGVPTICCPPRST
KIIDFKLPAPAKLRIRPPAHAGDQAYRDKHYKAMELMKALPDDDPRSFKQQGAVHCAYCD
GAYDQVGFPELELQIHNSWLFFPLHRYYLYFFEKILGKLINDPTFAGPFWNWDSPAGMPL
PAIYADPKSPLYDKLRSAQHQPPTLVDLDYNGTEDNVSKETTINANLKIMYRQMVSNSKN
AKLFFGNPYRAGDEPDPGGGSIEGTPHAPVHLWTGDNTQPNFEDMGNFYSAGRDPIFFAH
HSNVDRMWSIWKTLGGKRADLTDSDWLDSGFLFYNENAELVRVKVRDCLETKNLGYVYQD
VDIPWLSSKPTPRRAKVALSKIAKKLGVAHAAVASSSKVVAGTEFPINLGSKISTVVKRP
KQKKRSKKAKEDEEEILVIEGIEFDRDVAVKFDVYVNDVDDLPSGPDKTEFAGSFVSVPH
SHKHKKKMNTILRLGLTDLLEEIEAEDDDSVVVTLVPKFGAVKIGGIKIEFAS

================================================================================
