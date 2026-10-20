"""Conferência reproduzível. Dependências: numpy, scipy, matplotlib.
Execute da pasta Provas: python verificacao/calculos_e_figuras.py
Curvas são amostras das raízes de D(s)+K*N(s), não desenhos manuais.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import signal
from scipy.optimize import linear_sum_assignment

BASE = Path(__file__).resolve().parents[1]
FIG = BASE / 'figuras'
FIG.mkdir(exist_ok=True)
plt.rcParams.update({'font.size': 10, 'axes.grid': True, 'grid.alpha': .22,
                     'figure.dpi': 150, 'savefig.bbox': 'tight'})
results = {}

def metrics(name, n, d, band=.01, end=80):
    t = np.linspace(0, end, 80001)
    t, y = signal.step((n, d), T=t)
    final = n[-1] / d[-1]
    outside = np.flatnonzero(np.abs(y-final) > band*abs(final))
    ts = float(t[outside[-1]+1]) if len(outside) and outside[-1]+1 < len(t) else None
    results[name] = {'polos': [[float(p.real), float(p.imag)] for p in np.roots(d)],
                     'Mp_percent': float(max(0, (max(y)-final)/abs(final)*100)),
                     'Ts_s': ts, 'banda': band, 'dt_s': float(t[1]-t[0])}
    return t, y

def locus(ax, n, d, title, lim, kmax=1000, negative=False, selected=None):
    n = np.asarray(n, float) * (-1 if negative else 1)
    # Include exact real branch points so a coarse gain grid cannot cut corners.
    critical = np.polysub(np.polymul(np.polyder(d),n),np.polymul(d,np.polyder(n)))
    extra = []
    for s in np.roots(np.trim_zeros(critical,'f')):
        if abs(s.imag)<1e-6 and abs(np.polyval(n,s.real))>1e-10:
            gain = -np.polyval(d,s.real)/np.polyval(n,s.real)
            if 0<gain<kmax:extra.extend(gain*np.array([.999999,1,1.000001]))
    ks = np.unique(np.r_[0,np.geomspace(1e-7,kmax,3500),extra])
    trajectories = []
    prev = None
    for k in ks:
        roots = np.roots(np.polyadd(d, k*n)).astype(complex)
        if prev is not None:
            _, order = linear_sum_assignment(abs(prev[:, None]-roots[None, :]))
            roots = roots[order]
        trajectories.append(roots)
        prev = roots
    a = np.array(trajectories)
    for j in range(a.shape[1]):
        ax.plot(a[:, j].real, a[:, j].imag, color='#187b98', lw=1.5)
        # Arrow along each branch, within the displayed window when possible.
        valid = np.flatnonzero((a[:, j].real > lim[0]) & (a[:, j].real < lim[1]) &
                              (abs(a[:, j].imag) < lim[3]))
        if len(valid) > 20:
            q = valid[int(len(valid)*.8)]
            q0 = max(0, q-6)
            ax.annotate('', xy=(a[q,j].real,a[q,j].imag), xytext=(a[q0,j].real,a[q0,j].imag),
                        arrowprops=dict(arrowstyle='->',color='#187b98'))
    poles, zeros = np.roots(d), np.roots(n)
    ax.scatter(poles.real,poles.imag,marker='x',s=60,c='#242b3b',label='Polos MA',zorder=4)
    if len(zeros): ax.scatter(zeros.real,zeros.imag,facecolors='white',edgecolors='#bd4f31',s=55,label='Zeros MA',zorder=5)
    if selected is not None:
        r=np.roots(np.polyadd(d,selected*n))
        ax.scatter(r.real,r.imag,marker='*',s=95,c='#c48300',label=f'Polos MF: |K|={selected:g}',zorder=6)
    ax.axvline(0,color='gray',lw=.8);ax.axhline(0,color='gray',lw=.8)
    ax.set(xlim=lim[:2],ylim=lim[2:],xlabel='Re(s) [1/s]',ylabel='Im(s) [rad/s]',title=title)
    ax.legend(fontsize=7,loc='best')

def panel(name, specs, cols=2):
    rows=(len(specs)+cols-1)//cols
    fig,axs=plt.subplots(rows,cols,figsize=(6.3*cols,4.4*rows),squeeze=False)
    for ax,spec in zip(axs.flat,specs): locus(ax,**spec)
    for ax in list(axs.flat)[len(specs):]:ax.set_visible(False)
    fig.tight_layout();fig.savefig(FIG/name);plt.close(fig)

def sp(n,d,title,lim=(-8,2,-7,7),**kwargs):return dict(n=n,d=d,title=title,lim=lim,**kwargs)

panel('2023_1_lgr.png',[
    sp([1,-2],[1,2,0],'Q1: P com K > 0',(-7,4,-4,4)),
    sp([1,-2],[1,2,0],'Q1: P com K < 0 (complementar)',(-4,7,-4,4),negative=True),
    sp([100,116.1722069],[1,8,37,50,0],'Q2: PI, zero em -1,16172',(-9,3,-10,10),selected=1.107),
    sp(np.polymul([100,116.1722069],[1,5]),[1,8,37,50,0],'Q2: PID, zero adicional em -5',(-9,3,-14,14))])

for term,d,c,z in [('2024_1',[1,6,11,6,0],6,1),('2024_2',[1,8,19,12,0],6,1),('2025_2',[1,11,38,40,0],10,2)]:
    reduced=np.polydiv(d,[1,z])[0]
    panel(term+'_lgr.png',[
        sp([c],d,'P: quatro polos e nenhum zero',(-7,2,-5,5)),
        sp([c],reduced,f'PD: cancelamento estável em -{z}',(-8,2,-5,5))])

panel('2024_1_variacoes_zero.png',[
    sp([6,1.2],[1,6,11,6,0],'PD: z = 0,2 (zero próximo da origem)',(-6,2,-4,4)),
    sp([6,6],[1,6,11,6,0],'PD: z = 1 (polo e zero coincidentes)',(-6,2,-4,4)),
    sp([6,12],[1,6,11,6,0],'PD: z = 2',(-6,2,-4,4)),
    sp([6,30],[1,6,11,6,0],'PD: z = 5',(-7,3,-5,5))])

panel('2025_1_lgr.png',[
    sp([81,405],[1,22,145,264,0],'Q1: PI, z = 5; ganho externo unitário',(-16,4,-9,9),selected=1),
    sp([40],[1,8,52],'Q3: P positivo',(-20,2,-15,15)),
    sp([40,400],[1,8,52],'Q3: PD, z = 10',(-30,2,-12,12)),
    sp([40,80],[1,8,52,0],'Q3: PI, z = 2',(-12,2,-16,16)),
    sp([40,480,800],[1,8,52,0],'Q3: PID, zeros em -2 e -10',(-30,2,-12,12))])
panel('2025_2_pi.png',[sp(np.polymul([1,3.0231],[1,4]),[1,4,4,0],
    'Q2: PI, z = 3,0231; planta com zero em -4',(-12,2,-9,9),selected=6.223)],cols=1)
panel('revisao_pd_corrigido.png',[
    sp([1,4,3],[1,5,2,10,0],'Revisão: z = 1; K = 1 é instável',(-6,2,-5,5),selected=1),
    sp([1,3.2,.6],[1,5,2,10,0],'Revisão corrigida: z = 0,2',(-6,2,-5,5),selected=1)])

Pcr=2*np.pi/np.sqrt(11);kp=1.44;ki=kp/(Pcr/2);kd=kp*.33*Pcr
panel('2026_1_lgr.png',[
    sp([10,10*kp/kd,10*ki/kd],[1,7,11,5,0],'Q1: PID NO-OV',(-7,2,-5,5),selected=kd),
    sp([10],[1,5,0],'Q1: PID com dois zeros em -1',(-7,2,-5,5),selected=.625),
    sp([1],[1,4,8,0],'Q2: I',(-7,3,-6,6),selected=32),
    sp([1,1.6],[1,4,8,0],'Q2: PI, z = 1,6',(-7,3,-6,6)),
    sp([1,3.6,3.2],[1,4,8,0],'Q2: PID, zeros em -1,6 e -2',(-10,2,-5,5),selected=10)])

regions=[('2024_1',10,2,lambda k:(-k*k+9*k+10)/(6*k)),
         ('2024_2',70/3,4,lambda k:(-9*k*k+192*k+420)/(96*k)),
         ('2025_1',38.4,10,lambda k:(-25*k*k+885*k+2880)/(405*k)),
         ('2025_2',37.8,8,lambda k:(-k*k+33.8*k+151.2)/(12.1*k))]
for term,km,c,f in regions:
    k=np.linspace(.03,km,3000);lo=c/k;hi=f(k)
    fig,ax=plt.subplots(figsize=(8,4.5))
    ax.plot(k,lo,color='#20779b',label=f'Erro: z ≥ {c}/K (fronteira incluída)')
    ax.plot(k,hi,'--',color='#b44c35',label='Estabilidade: z < limite (excluída)')
    ax.fill_between(k,lo,hi,where=hi>lo,color='#6db994',alpha=.4,label='Interseção viável')
    ax.set(xlim=(0,km),ylim=(0,6),xlabel='K (ganho do PD)',ylabel='z (zero em -z)',title=term.replace('_','.')+' — estabilidade e erro de rampa')
    ax.legend(fontsize=8);fig.tight_layout();fig.savefig(FIG/(term+'_regiao.png'));plt.close(fig)

fig,ax=plt.subplots(figsize=(8,4.5));k=np.linspace(-15,20,500)
ax.plot(k,8*k+120,'--',color='#b44c35',label='Ki = 8Kp + 120 (excluída)')
ax.fill_between(k,0,8*k+120,color='#6db994',alpha=.4,label='0 < Ki < 8Kp + 120')
ax.scatter([1+15/.5387/4],[15/.5387],label='Projeto da Q3c',color='black')
ax.set(xlabel='Kp',ylabel='Ki',title='2023.2 Q3 — região estável',ylim=(0,300));ax.legend(fontsize=8)
fig.tight_layout();fig.savefig(FIG/'2023_2_regiao.png');plt.close(fig)

cases=[('2025.1_PI',[80.998,404.99],[1,22,145,344.998,404.99],.02),
       ('2025.2_P_1.68',[16.8],[1,11,38,40,16.8],.01),
       ('2025.2_P_8',[80],[1,11,38,40,80],.01),
       ('2025.2_PD_1.73',[17.3],[1,9,20,17.3],.01),
       ('2025.2_PI',np.polymul([6.223,6.223*3.0231],[1,4]),
        np.polyadd([1,4,4,0],np.polymul([6.223,6.223*3.0231],[1,4])),.02),
       ('2026.1_NOOV',[10*kd,10*kp,10*ki],[1,7,11+10*kd,5+10*kp,10*ki],.01),
       ('2026.1_PID_LGR',[6.25],[1,5,6.25],.01),
       ('2024.1_PD_K2',[12],[1,5,6,12],.01)]
for name,n,d,band in cases:metrics(name,n,d,band)
fig,ax=plt.subplots(figsize=(9,4.5))
for idx,label in [(5,'PID NO-OV'),(6,'PID pelo LGR')]:
    _,n,d,band=cases[idx];t=np.linspace(0,16,16001);t,y=signal.step((n,d),T=t);ax.plot(t,y,label=label,lw=1.8)
ax.axhspan(.99,1.01,color='#6db994',alpha=.3,label='Banda de 1%')
ax.set(xlabel='t [s]',ylabel='y(t)',title='2026.1 Q1 — resposta completa ao degrau');ax.legend()
fig.tight_layout();fig.savefig(FIG/'2026_1_degrau.png');plt.close(fig)

# Limites obtidos das inequações, não de varredura gráfica.
results['intersecoes_PD']={t:[float(x) for x in np.roots(c)] for t,c in [
    ('2024.1',[1,-9,2]),('2024.2',[9,-192,-36]),('2025.1',[25,-885,1170]),('2025.2',[1,-33.8,-54.4])]}
results['ganhos_criticos_P']={'2024.1':5/3,'2024.2':4.375,'2025.2':40*378/1210}
for term,d,c in [('2024.1',[1,6,11,6,0],6),('2024.2',[1,8,19,12,0],6),('2025.2',[1,11,38,40,0],10)]:
    breaks=np.roots(np.polyder(d));results[term+'_saidas']=[{'s':float(x),'K':float(-np.polyval(d,x)/c)} for x in breaks]
    assert all(np.real(np.roots(np.polyadd(d,[c*results['ganhos_criticos_P'][term]*.99])))<0)
    assert any(np.real(np.roots(np.polyadd(d,[c*results['ganhos_criticos_P'][term]*1.01])))>0)
assert abs(results['2025.1_PI']['Mp_percent']-5.27)<.02
assert abs(results['2026.1_PID_LGR']['Ts_s']-2.655)<.003
assert np.all(np.real(np.roots([1,4+10,8+3.6*10,3.2*10]))<0)
# Conferir as regiões pela localização independente das raízes.
for term,km,c,f in regions:
    plant={'2024_1':(6,[1,6,11,6,0]),'2024_2':(6,[1,8,19,12,0]),
           '2025_1':(5,[1,9,23,15,0]),'2025_2':(10,[1,11,38,40,0])}[term]
    A,D=plant
    for kval in np.linspace(.15,km*.99,24):
        for zval in [.1,.3,.7,1.2,2,4,8]:
            predicted=zval<f(kval)
            numerical=np.all(np.real(np.roots(np.polyadd(D,[A*kval,A*kval*zval])))<0)
            assert predicted==numerical,(term,kval,zval)
# Casos que exigiram correção do manuscrito.
for kval in [1e-3,.1,1,10,100,10000]:
    assert np.all(np.real(np.roots([1,5,2+kval,10+3.2*kval,.6*kval]))<0)
assert any(np.real(np.roots([1,5,3,14,3]))>0)  # z=1, K=1
assert np.all(np.real(np.roots([1,5,2+100/3,10+4*100/3,100]))<0)
assert np.max(abs(np.sort_complex(np.roots([1,50,400,20000]))-
                  np.sort_complex(np.array([-50,20j,-20j]))))<1e-9
Ki=15/.5387;Kp=1+Ki/4
assert np.allclose([1,8,15+Kp,Ki],np.polymul([1,4],[1,4,Ki/4]))
results['validacao']='Limites P, regiões PD, fatoração de 2023.2 e correção da revisão conferidos por raízes.'
(BASE/'verificacao/resultados_numericos.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(f'{len(list(FIG.glob("*.png")))} figuras; conferências numéricas aprovadas.')
