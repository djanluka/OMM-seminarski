# OMM-seminarski

Lotka Voltera model: <br>
dX/dt = a*X - b*X*Y <br>
dY/dt = -c*Y + d*X*Y

a - natalitet vrste(alge, ljudi ili slicno) <br>
b - umanjenje vrste pod uticajem toksina <br>
c - mortalitet toksina <br>
d - stopa nastajanje toksina u zavisnosti od vrste <br>

***
<h3> Početni model </h3> 
Za početne parametre uzete su jednake vrednosti koje mi aproksimiraju neku zlatnu sredinu. Ovo je osnovni model na kom možemo videti kako se kroz vreme menjaju populacije algi i toksina. Početne vrednosti za alge i toksine su redom 2 i 1 (možemo ih posmatrati u hiljadama jedinki) i to samo znači da u početnom trenutku imamo dva puta više algi nego toksina. Na modelu možemo videti (time=10) kako se prilikom povećanja populacije postepeno povećava broj toksina do tačke optimuma (time=~12) kada zbog uticaja toksina počinje polako da opada populacija algi, a ubrzo nakon toga (time=~15) počinje i opadanje toksina jer se smanjuje broj algi od kojih oni zavise. Ovo je kružni proces koji traje kroz vreme.

![plot](./plots/model.png "Model")

***
<h3> a </h3> 

Kada povećamo natalitet algi, možemo primetiti da alge za nijansu prelaze granicu 2 sa leve strane, ali je mnogo bitnije primetiti povećanje koncentrancije toksina, jer što je više algi to će se više toksina stvoriti. 
![plot](./plots/aIn.png )

Kada smanjimo natalitet algi, možemo primetiti spor rast populacije algi što je očigledno na osnovu širokog levka koje pravi crvena linija. U skladu sa njom i plava linija sporo raste što znači da broj toksina prati populaciju algi.
![plot](./plots/aDec.png)

***
<h3> b </h3> 

Kada povećamo uticaj toksina na smrtnost algi, vidimo da crvena linija ima učestaliju frekvenciju što znači da nakon nastanka alge brzo izumiru. Zbog brzog izumiranja algi vidimo da se toksini ne mogu previše razviti.
![plot](./plots/bIn.png )

Kada smanjino uticaj koje toksini imaju na smrtnost algi, to znači da će alge duže živeti. Sporu smrtnost algi možemo videti na osnovu širok levka koji pravi crvena linija. U skladu sa tim se povećava broj toksina kroz vreme jer alge duže žive i proizvode toksine.
![plot](./plots/bDec.png )

***
<h3> c </h3> 

Kada se poveća mortalitet toksina, vidimo da plava linija ne dostiže visoke vrednosti, odnosno toksini brzo izumiru. Takođe vidimo da populacija algi normalno funkcioniše i zbog brzog izumiranja toksina broj algi se jako slabo smanjuje i varira između 1.3 i 2. 
![plot](./plots/cIn.png )

Kada smanjimo mortalitet toksina, oni duže žive i utiču na smrtnost algi. Zbog toga crvena linija, koja aproksimira alge, prilazi nuli i faktički imamo izumiranje vrste. Kod plave linije vidimo da se sporo spušta što odgovara tome da toksini imaju nizak mortalitet.
![plot](./plots/cDec.png)

***
<h3> d </h3> 

Kada povećamo nastajanje toksina, vidimo kako plava linija prelazi granicu 3, a setimo se da je na početku bila oko 2.

![plot](./plots/dIn.png)

Kada smanjimo nastajanje toksina, vidimo kako se toksini kreću oko granice 1. Takođe zbog malog broja toksina, povećava se koncentrancija algi do granice 3.

![plot](./plots/dDec.png)
***
<h3> Razni modeli </h3>

Možemo smatrati da je natalitet algi i više nego dobar (a>0.5) i da alge prozvode neznatan broj toksina (d<0.5). Kada toksini nastanu, oni brzo izumiru (c>0.5) i uticaj toksina na smrtnost algi nije toliko jak (b<0.5). Model prikazuje da zbog dobrog nataliteta i malog uticaja toksina, alge dostižu visoku vrednost preko 7. Za toksine možemo videti da su u 1:2 odnosu naspram algi, što je u skladu sa počentim tačkama. Teško nastaju, brzo izumiru, ali zbog velikog broja algi uvek će ih biti.
![plot](./plots/model1.png)

U drugom modelu za natalitet imamo istu pretpostavku. Isto važi i za nastajanje toksina. Međutim, u ovom primeru imamo mnogo jači uticaj toksina na smrtnost algi (b>0.5) plus toksini sporije izumiru (c<0.5). Na osnovu ovoga, vidimo da toksini nadvladavaju nad algama. 
![plot](./plots/model2.png)

