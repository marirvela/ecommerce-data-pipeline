# Resumen Ejecutivo y Recomendaciones Estrategicas
**Analista:** Mariana Rodriguez Velandia  
**Tipo de Proyecto:** Caso de Estudio End-to-End (Data Pipeline yEstrategia)  

## Contexto
Para ser 100% transparente, los datos que ves en este dashboard son simulados. No quise simplemente entrar a Kaggle, descargar un Excel perfectamente limpio y conectarlo a Power BI. Así no es como funciona el mundo real. Yo sé que en la realidad los datos con los que uno trabaja no viene ya listos para ser modelados ni mucho menos, detras habran gran variedad de procesos para poder llegar a eso.

Por lo tanto en su lugar, programé scripts en Python (`generate_data.py` y `generate_marketing.py`) para generar un entorno de e-commerce realista y caótico directamente desde mi terminal. Quería demostrar que mis habilidades van mucho más allá de "hacer gráficas bonitas". Puedo manejar todo el ciclo de vida del dato: generar la data cruda, armar un pipeline ETL para limpiar el desorden (valores nulos, formatos de fecha rotos), modelarlo en SQLite, y finalmente diseñar una interfaz gerencial.

Y hablando de la interfaz: elegí especificamente un diseño Dark Mode tipo FinTech porque la carga cognitiva de los ejecutivos importa. Cuando un CEO mira una pantalla, los números que mueven la aguja del negocio deben saltar a la vista de inmediato.

Ahora, pongamonos la camiseta de la empresa. Si este fuera un e-commerce real para el que trabajo así es exactamente como le presentaria estos resultados al equipo directivo:

---

## Primero: El Escenario de Negocio (Caso Ficticio: 2025-2026)
Durante el último año (Mayo 2025 a Marzo 2026, como se ve en la gráfica de tendencia), escalamos nuestras campañas digitales en multiples plataformas para impulsar las ventas internacionales. El objetivo de este reporte es simple: entender qué funciona, cortar lo que nos hace perder dinero, y decidir dónde poner el presupuesto.

### Segundo: Analisis Profundo KPIs

#### 1. El ROI es como sospechosamente bueno (915.86%)
Gastamos $11 millones en pauta publicitaria (Ad Spend) y generamos $113 millones en ventas totales. Basicamente, por cada dolar que metimos a la máquina, sacamos mas de $9. Honestamente un ROI tan alto indica que nuestro costo de adquisición de clientes (CAC) es muy saludable pero tambien significa que estamos siendo demasiado conservadores. Cuando el ROI supera el 900%, significa que el mercado tiene mucho mas apetito por asi decirlo del presupuesto que le estamos dando. Aun no tocamos techo.

#### 2. El Mix de Medios: Meta y Google cargan con el peso pesado
Si miramos la distribución de plataformas, Meta Ads (43.49%) y Google Ads (27.71%) se estan comiendo cerca del 70% del presupuesto. Basado en el volumen de ingresos, es evidente que son los canales que mejor convierten. Sin embargo, el elefante en la habitacion es LinkedIn Ads (15.94%). A menos que seamos una empresa B2B vendiendo software corporativo carisimo, gastar $2 millones en LinkedIn es probablemente un desperdicio brutal de recursos debido a sus altos costos por impresión (CPM).

#### 3. La sorpresa geográfica: Somos gigantes en LATAM y Mercados Emergentes
Si revisamos el Top 5 de países, no estamos liderando en EEUU ni en Europa occidental. Nuestro comprador numero uno es *Nepal*, seguida respirandole en la nuca por Bolivia y Argentina. Francia y Bielorrusia quedan mas atras. Marketing hizo un trabajo fantastico capturando estos mercados, pero esto ya no es un insight de marketing—es un reto de operaciones. ¿Estan nuestros centros de distribución optimizados para envios a Sudamérica? ¿Los costos de logistica se estan comiendo nuestro margen de ganancia ahí?

#### 4. La volatilidad en la tendencia de ventas (Time-Series)
Echa un vistazo a la linea verde neón en la parte inferior del dashboard. Aunque el volumen general es masivo, las ventas del día a día son altamente volatiles. Hay picos gigantes seguidos de caídas abruptas. Esto me sugiere que nuestros ingresos dependen demasiado de "ventas flash", promociones de fin de semana o inyecciones de pauta muy especificas, en lugar de tener una base solida de ventas organicas recurrentes.

---

### Ahora ¿Qué deberíamos hacer? 

Si yo estuviera a cargo de la estrategia de datos, no me limitaria a enviar este reporte y dar todo por terminado. Presionaria para que se tomen estas decisiones de negocio de inmediato:

1. **Abrir la billetera para Meta Ads sin miedo:** Estamos dejando dinero sobre la mesa. Necesitamos escalar nuestra inversión en Meta y Google un 20-30% el proximo mes. Seguimos escalando hasta que ese ROI del 915% baje a un 400-500% más normalizado (el punto de rendimiento decreciente).
2. **Localizar toda la estrategia para Sudamérica:** Como Bolivia y Argentina dominan el Top 3, tenemos que apostar fuerte. Deberiamos adaptar los copys de los anuncios a modismos locales, asegurar que nuestro checkout acepte metodos de pago de la región, y renegociar contratos logisticos para los envios a latamm.
3. **Auditar la estrategia de LinkedIn y TikTok:** Recomiendo pausar las campañas de LinkedIn por un mes como prueba A/B para ver si las ventas totales caen. Si no lo hacen, reasignamos esos $2M de presupuesto permanentemente a TikTok Ads que hoy solo tiene el 12% del gasto pero probablemente nos da un alcance de marca (Top of Funnel) muchisimo mas barato.
4. **Construir un Dashboard de Retención (Siguientes Pasos):** Ahora mismo solo vemos ventas totales. Para mi proximo proyecto quiero analizar los datos del CRM. ¿Estos son compradores de una sola vez o están regresando? Necesitamos suavizar esa línea de ventas volatil enfocandonos en el valor de vida del cliente (LTV).

***
*¿Quieres ver cómo se preparó todo esto? En la carpeta `scripts/` de este repositorio se puede ver el codigo python(ETL) que hizo posible todo este estudio de caso ficticio*