"""Genera las páginas de estudio.treso.cl (español e inglés). Uso: python3 build.py"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
MAIL = 'contacto@treso.cl'
SITE = 'https://estudio.treso.cl'
UPDATED = {'es': '3 de noviembre de 2026', 'en': 'November 3, 2026'}
UPDATED_WD = {'es': '5 de noviembre de 2026', 'en': 'November 5, 2026'}
UPDATED_DD = {'es': '16 de noviembre de 2026', 'en': 'November 16, 2026'}
UPDATED_MK = {'es': '17 de noviembre de 2026', 'en': 'November 17, 2026'}

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@600;700&family=Inter:wght@400;500;700&family=Fira+Sans:wght@400;500;800&family=IBM+Plex+Mono:wght@400;500&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">')


def page(path, lang, title, desc, body_class, body, alt_href, depth, og='d40-hero'):
    up = '../' * depth
    html = f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{up}assets/logo.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{up}assets/apple-touch-icon.png">
<link rel="alternate" hreflang="{'en' if lang == 'es' else 'es'}" href="{SITE}{alt_href}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/assets/{og}-{lang}.jpg">
{FONTS}
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body class="{body_class}">
<a class="skip" href="#main">{'Ir al contenido' if lang == 'es' else 'Skip to content'}</a>
{body.replace('{up}', up)}
</body>
</html>
'''
    full = os.path.join(ROOT, path, 'index.html')
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf-8').write(html)
    print('ok', path or '/')


def studio_top(lang, alt):
    return f'''<div class="wrap"><header class="top">
  <a class="brand" href="{{up}}{'' if lang == 'es' else 'en/'}" aria-label="Estudio Treso"><img src="{{up}}assets/logo.svg" alt=""><span><small>ESTUDIO</small><b>TRESO</b></span></a>
  <nav class="topnav"><a class="lang" href="{{up}}{'contacto/' if lang == 'es' else 'en/contact/'}">{'CONTACTO' if lang == 'es' else 'CONTACT'}</a><a class="lang" href="{alt}" hreflang="{'en' if lang == 'es' else 'es'}">{'ENGLISH' if lang == 'es' else 'ESPAÑOL'}</a></nav>
</header></div>'''


def game_bar(lang, alt):
    home = '{up}' + ('' if lang == 'es' else 'en/')
    return f'''<div class="wrap"><header class="bar">
  <a class="mini" href="{home}"><img src="{{up}}assets/logo.svg" alt="">ESTUDIO TRESO</a>
  <a class="lang" href="{alt}" hreflang="{'en' if lang == 'es' else 'es'}">{'ENGLISH' if lang == 'es' else 'ESPAÑOL'}</a>
</header></div>'''


PRODUCT_NAME = {'depth40': 'Depth 40', 'widgetdesign': 'Widget Design', 'doce12': '12/12', 'kardek': 'My Kardek'}


def game_footer(lang, slug='depth40'):
    n = PRODUCT_NAME[slug]
    if lang == 'es':
        links = [('{up}', 'Todos los juegos y apps'), (f'{{up}}{slug}/', n), (f'{{up}}{slug}/soporte/', 'Soporte'),
                 (f'{{up}}{slug}/privacidad/', 'Privacidad'), (f'{{up}}{slug}/terminos/', 'Términos')]
    else:
        links = [('{up}en/', 'All games and apps'), (f'{{up}}{slug}/en/', n), (f'{{up}}{slug}/support/', 'Support'),
                 (f'{{up}}{slug}/privacy/', 'Privacy'), (f'{{up}}{slug}/terms/', 'Terms')]
    nav = ''.join(f'<a href="{h}">{t}</a>' for h, t in links)
    return f'''<div class="wrap"><footer><span>© 2026 TRESO SPA · Santiago, Chile</span><nav>{nav}</nav></footer></div>'''


# ---------------------------------------------------------------- tiendas
# Enlace de descarga por plataforma: None = "Próximamente". Cuando cada tienda publique la app, pegar aquí su enlace.
#   Google Play: https://play.google.com/store/apps/details?id=cl.treso.depth40
#   App Store:   https://apps.apple.com/app/id<número> (lo da App Store Connect)
STORES = {
    'depth40': {'android': 'https://play.google.com/store/apps/details?id=cl.treso.depth40', 'ios': None},
    'widgetdesign': {'android': 'https://play.google.com/store/apps/details?id=cl.treso.widgetdesign', 'ios': None},
    'doce12': {'android': 'https://play.google.com/store/apps/details?id=cl.treso.doce12', 'ios': None},
    # My Kardek: cuando Google Play la publique → 'https://play.google.com/store/apps/details?id=cl.treso.fichero'
    'kardek': {'android': None, 'ios': None},
}
PLAT = {'android': ('Google Play', 'Android'), 'ios': ('App Store', 'iPhone')}


def platforms_line(slug, lang):
    """Una etiqueta por plataforma: DISPONIBLE EN ANDROID · IPHONE PRÓXIMAMENTE."""
    st = STORES[slug]
    es = lang == 'es'
    live = [PLAT[k][1] for k in ('android', 'ios') if k in st and st[k]]
    soon = [PLAT[k][1] for k in ('android', 'ios') if k in st and not st[k]]
    join = ' y ' if es else ' and '
    parts = []
    if live:
        parts.append(('DISPONIBLE EN ' if es else 'AVAILABLE ON ') + join.join(live).upper())
    if soon:
        s = join.join(soon).upper()
        parts.append((s + ' PRÓXIMAMENTE') if es else (s + ' COMING SOON') if live else ('COMING SOON · ' + s))
        if es and not live:
            parts[-1] = 'PRÓXIMAMENTE · ' + s
    return ' · '.join(parts)


def store_buttons(slug, lang):
    out = ''
    for k in ('android', 'ios'):
        if k not in STORES[slug]:
            continue
        store, dev = PLAT[k]
        url = STORES[slug][k]
        if url:
            top = 'DESCARGAR EN' if lang == 'es' else 'GET IT ON'
            out += f'<a class="store" href="{url}" rel="noopener"><small>{top}</small><b>{store}</b><span>{dev}</span></a>'
        else:
            top = 'PRÓXIMAMENTE EN' if lang == 'es' else 'COMING SOON TO'
            out += f'<span class="store off" aria-disabled="true"><small>{top}</small><b>{store}</b><span>{dev}</span></span>'
    return '<div class="stores">' + out + '</div>'


# ---------------------------------------------------------------- inicio del estudio
# Catálogo: cada juego o app tiene su carpeta (/slug/, /slug/en/, /slug/soporte/, /slug/privacidad/ ...).
# Para agregar uno nuevo: sumarlo aquí y crear sus páginas abajo, igual que Depth 40.
CATALOG = [
    dict(slug='depth40', kind={'es': 'JUEGO', 'en': 'GAME'}, name='DEPTH <em>40</em>', label='Depth 40', pic='d40-hero',
         p={'es': 'Sigilo en submarino, desde adentro. Ocho misiones bajo el mar y el hielo al mando de la sala de control: sonar, periscopio, timón, máquinas, profundidad y torpedos. Nunca ves tu submarino desde afuera; lo comandas como un capitán de verdad.',
            'en': 'Submarine stealth, from the inside. Eight missions under the sea and the ice, in command of the control room: sonar, periscope, helm, engines, depth and torpedoes. You never see your submarine from outside; you command it like a real captain.'},
         ),
    dict(slug='widgetdesign', kind={'es': 'APP', 'en': 'APP'}, name='WIDGET <em>DESIGN</em>', label='TRESO: Widget Design', pic='wd-hero', cls=' wd',
         p={'es': 'Ocho estilos de widgets para tu pantalla de inicio. Cada uno es un kit de cuatro piezas que calzan entre sí: hora, clima, batería, agenda y más.',
            'en': 'Eight widget styles for your Home Screen. Each one is a kit of four pieces that fit together: time, weather, battery, calendar and more.'},
         ),
    dict(slug='doce12', kind={'es': 'APP', 'en': 'APP'}, name='12<em>/</em>12', label='12/12: Diario de cultivo', pic='dd-card', cls=' dd',
         p={'es': 'Diario de cultivo para carpas indoor. Tu carpa a escala, una bitácora de riegos, clima, luz y fotos, el avance del ciclo hasta la cosecha y un medidor de luz con el sensor del teléfono.',
            'en': 'A grow diary for indoor tents. Your tent to scale, a logbook of waterings, climate, light and photos, cycle progress up to harvest and a light meter using your phone’s sensor.'},
         ),
    dict(slug='kardek', kind={'es': 'APP', 'en': 'APP'}, name='MY <em>KARDEK</em>', label='My Kardek', pic='mk-card', cls=' mk',
         p={'es': 'Un fichero de notas en tu teléfono: cuatro cajones que abres y cierras, y fichas que sacas, escribes y vuelves a guardar. Desde una hoja de cuaderno hasta 48 plantillas listas para usar.',
            'en': 'A note card file on your phone: four drawers you open and close, and cards you take out, write on and put back. From a blank notebook page to 48 ready-made templates.'},
         ),
]
STUDIO = {
    'es': dict(h1='Juegos y apps para tu teléfono.', lead='Estudio Treso es el estudio de TRESO SPA, en Santiago de Chile. Hacemos juegos y aplicaciones para Android y iPhone.',
               cat='NUESTROS JUEGOS Y APPS', go='VER MÁS ›', more_k='EN CAMINO', more='Más juegos y apps en desarrollo. Pronto aquí.', contact='Contacto'),
    'en': dict(h1='Games and apps for your phone.', lead='Estudio Treso is the studio of TRESO SPA, in Santiago, Chile. We make games and apps for Android and iPhone.',
               cat='OUR GAMES AND APPS', go='LEARN MORE ›', more_k='ON THE WAY', more='More games and apps in development. Coming here soon.', contact='Contact'),
}
for lang, t in STUDIO.items():
    path = '' if lang == 'es' else 'en'
    alt = '{up}en/' if lang == 'es' else '{up}'
    cards = ''
    for c in CATALOG:
        href = '{up}' + c['slug'] + ('/' if lang == 'es' else '/en/')
        cards += f'''
  <a class="game-card{c.get('cls', '')}" href="{href}">
    <div class="pic" style="background-image:url('{{up}}assets/{c['pic']}-{lang}.jpg')" role="img" aria-label="{c['label']}"></div>
    <div class="txt"><span class="k">{c['kind'][lang]} · {platforms_line(c['slug'], lang)}</span><h2>{c['name']}</h2><p>{c['p'][lang]}</p><span class="go">{t['go']}</span></div>
  </a>'''
    body = studio_top(lang, alt) + f'''
<main id="main" class="wrap">
  <h1>{t['h1']}</h1>
  <p class="lead">{t['lead']}</p>
  <h2 class="cat">{t['cat']}</h2>
  <div class="catalog">{cards}
    <div class="soon-card"><span class="k">{t['more_k']}</span><p>{t['more']}</p></div>
  </div>
</main>
<div class="wrap"><footer><span>© 2026 TRESO SPA · Santiago, Chile</span><span><a href="{{up}}{'contacto/' if lang == 'es' else 'en/contact/'}">{t['contact']}</a> · <a href="mailto:{MAIL}">{MAIL}</a></span></footer></div>'''
    page(path, lang, 'Estudio Treso', t['lead'], 'studio', body, '/en/' if lang == 'es' else '/', 0 if lang == 'es' else 1)

# ---------------------------------------------------------------- Contacto
COMPANY = dict(name='TRESO SPA', addr='Avenida Perú 1030, Santiago, Chile')
CONTACT = {
    'es': dict(path='contacto', alt='/en/contact/', h1='Contacto', lead='Estudio Treso es el estudio de juegos y aplicaciones de TRESO SPA. Escríbenos por cualquier consulta sobre nuestros juegos, apps, soporte o privacidad.',
               rows=[('Empresa', 'TRESO SPA'), ('Dirección', COMPANY['addr']), ('Correo', f'<a href="mailto:{MAIL}">{MAIL}</a>'), ('Sitio', '<a href="https://estudio.treso.cl">estudio.treso.cl</a>')],
               sup_h='SOPORTE POR APP', sup=[('Depth 40', '{up}depth40/soporte/'), ('Widget Design', '{up}widgetdesign/soporte/'), ('12/12', '{up}doce12/soporte/'), ('My Kardek', '{up}kardek/soporte/')]),
    'en': dict(path='en/contact', alt='/contacto/', h1='Contact', lead='Estudio Treso is the games and apps studio of TRESO SPA. Write to us about our games, apps, support or privacy.',
               rows=[('Company', 'TRESO SPA'), ('Address', COMPANY['addr']), ('Email', f'<a href="mailto:{MAIL}">{MAIL}</a>'), ('Website', '<a href="https://estudio.treso.cl">estudio.treso.cl</a>')],
               sup_h='SUPPORT BY APP', sup=[('Depth 40', '{up}depth40/support/'), ('Widget Design', '{up}widgetdesign/support/'), ('12/12', '{up}doce12/support/'), ('My Kardek', '{up}kardek/support/')]),
}
for lang, t in CONTACT.items():
    alt = '{up}' + t['alt'].lstrip('/')
    rows = ''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in t['rows'])
    sup = ''.join(f'<li><a href="{h}">{n}</a></li>' for n, h in t['sup'])
    body = studio_top(lang, alt) + f'''
<main id="main" class="wrap contact">
  <h1>{t['h1']}</h1>
  <p class="lead">{t['lead']}</p>
  <dl>{rows}</dl>
  <h2 class="cat">{t['sup_h']}</h2>
  <ul class="sup">{sup}</ul>
</main>
<div class="wrap"><footer><span>© 2026 TRESO SPA · {COMPANY['addr']}</span><span><a href="mailto:{MAIL}">{MAIL}</a></span></footer></div>'''
    page(t['path'], lang, f"{t['h1']} · Estudio Treso", t['lead'], 'studio', body, t['alt'], 1 if lang == 'es' else 2)

# ---------------------------------------------------------------- Depth 40
D40 = {
    'es': dict(
        tag='SIGILO EN SUBMARINO',
        intro=['Eres el capitán. Desde la consola de mando decides el rumbo, la velocidad y la profundidad. Cada ruido que haces puede delatarte.',
               'Depth 40 es un juego de sigilo en primera persona dentro de un submarino. Nunca lo ves desde afuera: todo lo que sabes del mar te llega por el sonar, el periscopio y tu instinto.'],
        pills=['8 MISIONES', 'ESPAÑOL · ENGLISH', '2 MISIONES GRATIS', 'PAGO ÚNICO', 'SIN ANUNCIOS', 'JUEGA SIN INTERNET'],
        shots_h='CAPTURAS', feat_h='LA CONSOLA',
        feats=[('Sonar pasivo y activo', 'Escucha sin ser oído. El ping da distancias exactas, pero te delata.'),
               ('Periscopio', 'La única vista real del exterior, y solo a cota 20 m. De noche, con visión nocturna.'),
               ('Modo silencio', 'Apaga todo lo que hace ruido y espera a que el enemigo deje de buscarte.'),
               ('Armas', 'Torpedos rectos y filoguiados, misil, señuelos y ametralladora.')],
        mis_h='PRIMERA TEMPORADA', mis=['Aguas ajenas', 'Blanco quieto', 'Blanco en movimiento', 'Cazador', 'Rescate bajo el hielo', 'Pesqueros', 'Señuelo', 'Orden sellada'],
        alt='Capturas de Depth 40', shots=['inicio', 'periscopio', 'nocturna', 'consola', 'misiones', 'brief', 'hielo'],
        shot_alt=['Menú principal', 'Periscopio frente a la base naval enemiga', 'Periscopio con visión nocturna leyendo el casco de un pesquero', 'Consola de mando', 'Archivador de misiones', 'Instrucciones de la misión 4', 'Misión 8 bajo el hielo'],
        desc='Depth 40: sigilo en submarino. Ocho misiones para Android y iPhone. Un juego de Estudio Treso.'),
    'en': dict(
        tag='SUBMARINE STEALTH',
        intro=['You are the captain. From the command console you set the heading, the speed and the depth. Every sound you make can give you away.',
               "Depth 40 is a first-person stealth game set inside a submarine. You never see it from outside: everything you know about the sea comes through sonar, periscope and instinct."],
        pills=['8 MISSIONS', 'ENGLISH · ESPAÑOL', '2 FREE MISSIONS', 'ONE-TIME PURCHASE', 'NO ADS', 'NO INTERNET NEEDED'],
        shots_h='SCREENSHOTS', feat_h='THE CONSOLE',
        feats=[('Passive and active sonar', 'Listen without being heard. A ping gives exact distances, but gives you away.'),
               ('Periscope', 'The only real view outside, and only at 20 m. At night, with night vision.'),
               ('Silent running', 'Shut down everything that makes noise and wait for the enemy to give up.'),
               ('Weapons', 'Straight and wire-guided torpedoes, a missile, decoys and a machine gun.')],
        mis_h='SEASON ONE', mis=['Foreign waters', 'Still target', 'Moving target', 'Hunter', 'Rescue under the ice', 'Fishing boats', 'Decoy', 'Sealed order'],
        alt='Depth 40 screenshots', shots=['inicio', 'periscopio', 'nocturna', 'consola', 'misiones', 'brief', 'hielo'],
        shot_alt=['Main menu', 'Periscope facing the enemy naval base', 'Night-vision periscope reading a fishing boat hull', 'Command console', 'Mission files', 'Mission 4 briefing', 'Mission 8 under the ice'],
        desc='Depth 40: submarine stealth. Eight missions for Android and iPhone. A game by Estudio Treso.'),
}
for lang, t in D40.items():
    path = 'depth40' if lang == 'es' else 'depth40/en'
    alt = '{up}depth40/en/' if lang == 'es' else '{up}depth40/'
    shots = ''.join(f'<img src="{{up}}assets/d40-{n}-{lang}.jpg" width="540" height="1080" loading="lazy" alt="{a}">' for n, a in zip(t['shots'], t['shot_alt']))
    feats = ''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in t['feats'])
    mis = ''.join(f'<li{" class=\"sealed\"" if i == 7 else ""}>{m.upper()}</li>' for i, m in enumerate(t['mis']))
    pills = ''.join(f'<span class="pill">{p}</span>' for p in t['pills'])
    body = game_bar(lang, alt) + f'''
<main id="main" class="wrap">
  <div class="hero" style="background-image:url('{{up}}assets/d40-hero-{lang}.jpg')" role="img" aria-label="Depth 40"></div>
  <h1>DEPTH <em>40</em></h1>
  <p class="tag">{t['tag']}</p>
  {''.join(f'<p class="intro">{p}</p>' for p in t['intro'])}
  {store_buttons('depth40', lang)}
  <div class="pills">{pills}</div>
  <h2>{t['shots_h']}</h2>
  <div class="shots" role="group" aria-label="{t['alt']}" tabindex="0">{shots}</div>
  <h2>{t['feat_h']}</h2>
  <div class="feat">{feats}</div>
  <h2>{t['mis_h']}</h2>
  <ol class="missions">{mis}</ol>
</main>
''' + game_footer(lang)
    page(path, lang, 'Depth 40 · Estudio Treso', t['desc'], 'game', body, '/depth40/en/' if lang == 'es' else '/depth40/', 1 if lang == 'es' else 2)

# ---------------------------------------------------------------- privacidad
PRIV = {
    'es': ('depth40/privacidad', 'Política de privacidad', 'Depth 40', f'Última actualización: {UPDATED["es"]}', [
        ('', 'Depth 40 es un juego desarrollado por Estudio Treso, marca de TRESO SPA (Santiago, Chile).'),
        ('Datos que recopilamos', 'Ninguno. Depth 40 no pide registro, no usa cuentas propias, no muestra publicidad y no nos envía información.'),
        ('Compra del juego completo', 'Las misiones 1 y 2 son gratis; las demás se desbloquean con una compra única dentro de la app. El pago lo procesa la tienda (Google Play o App Store) con tu cuenta de esa tienda, según su propia política de privacidad. Nosotros no recibimos tus datos de pago: el juego solo le pregunta a la tienda si la compra existe para abrir las misiones.'),
        ('Datos guardados en tu dispositivo', 'El juego guarda en tu propio teléfono el idioma elegido, tus ajustes (música, efectos, vibración, color de pantalla) y las misiones cumplidas. Esa información no sale del dispositivo, no la recibimos y se borra al desinstalar el juego o al usar «Reiniciar progreso» en Ajustes.'),
        ('Permisos', 'Depth 40 no usa cámara, micrófono, ubicación, contactos ni otros datos personales. La vibración se usa solo como efecto del juego y puede apagarse en Ajustes.'),
        ('Terceros', 'El juego no incluye servicios de análisis ni de publicidad. El único servicio externo es el sistema de compras de la tienda, usado solo para la compra del juego completo.'),
        ('Niños', 'El juego no está dirigido a menores de 13 años y no recopila datos de nadie.'),
        ('Cambios', 'Si esta política cambia, publicaremos la nueva versión en esta misma página con su fecha.'),
        ('Contacto', f'Para cualquier consulta sobre privacidad escríbenos a <a class="mail" href="mailto:{MAIL}">{MAIL}</a>'),
    ], '{up}depth40/privacy/', '/depth40/privacy/'),
    'en': ('depth40/privacy', 'Privacy Policy', 'Depth 40', f'Last updated: {UPDATED["en"]}', [
        ('', 'Depth 40 is a game developed by Estudio Treso, a brand of TRESO SPA (Santiago, Chile).'),
        ('Data we collect', 'None. Depth 40 requires no sign-up, has no accounts of its own, shows no ads and sends no information to us.'),
        ('Full game purchase', 'Missions 1 and 2 are free; the rest are unlocked with a one-time in-app purchase. Payment is processed by the store (Google Play or the App Store) with your store account, under the store’s own privacy policy. We never receive your payment details: the game only asks the store whether the purchase exists in order to open the missions.'),
        ('Data stored on your device', 'The game stores on your own phone the language you chose, your settings (music, effects, vibration, screen color) and the missions you completed. This information never leaves the device, we never receive it, and it is deleted when you uninstall the game or use “Reset progress” in Settings.'),
        ('Permissions', 'Depth 40 does not use the camera, microphone, location, contacts or any other personal data. Vibration is used only as a game effect and can be turned off in Settings.'),
        ('Third parties', 'The game includes no analytics or advertising services. The only external service is the store’s billing system, used only for the full game purchase.'),
        ('Children', 'The game is not directed at children under 13 and collects no data from anyone.'),
        ('Changes', 'If this policy changes, we will publish the new version on this same page with its date.'),
        ('Contact', f'For any privacy question, write to us at <a class="mail" href="mailto:{MAIL}">{MAIL}</a>'),
    ], '{up}depth40/privacidad/', '/depth40/privacidad/'),
}
for lang, (path, h1, k, meta, secs, alt, alt_abs) in PRIV.items():
    body_secs = ''.join((f'<h2>{h.upper()}</h2>' if h else '') + f'<p>{p}</p>' for h, p in secs)
    body = game_bar(lang, alt) + f'''
<main id="main" class="wrap doc">
  <h1>{h1.upper()}</h1>
  <p class="meta">{k} · {meta}</p>
  {body_secs}
</main>
''' + game_footer(lang)
    page(path, lang, f'{h1} · Depth 40', f'{h1} · Depth 40 · Estudio Treso', 'game', body, alt_abs, 2)

# ---------------------------------------------------------------- soporte
SUP = {
    'es': ('depth40/soporte', 'Soporte', 'Escríbenos y te respondemos lo antes posible. Si es un error, cuéntanos el modelo de tu teléfono, la misión y qué estabas haciendo.', [
        ('¿Cómo cambio el idioma?', 'En el menú principal, toca AJUSTES y elige ESPAÑOL o ENGLISH.'),
        ('No se escucha nada.', 'Revisa que el teléfono no esté en silencio y que en AJUSTES estén encendidas la música y los efectos. El sonido empieza al primer toque en la pantalla.'),
        ('¿Cómo vuelvo a ver el tutorial?', 'En AJUSTES, toca «Ver tutorial». Cada misión también tiene el botón VER TUTORIAL en sus instrucciones.'),
        ('Perdí mi avance.', 'El avance se guarda solo en tu teléfono. Si desinstalas el juego o borras sus datos, se pierde. «Reiniciar progreso» en AJUSTES también lo borra.'),
        ('¿Qué es gratis y qué se paga?', 'Las misiones 1 y 2 y el tutorial son gratis. Las misiones 3 a 8 se desbloquean con un pago único, sin anuncios ni suscripciones.'),
        ('Ya pagué y las misiones siguen bloqueadas.', 'Abre el juego con internet, ve a MISIONES › OBTENER y toca RESTAURAR COMPRA. Usa la misma cuenta de Google con la que compraste. Si el pago quedó pendiente, se abrirá cuando la tienda lo confirme.'),
        ('¿Necesito internet?', 'Solo para comprar o restaurar la compra. Para jugar, Depth 40 funciona sin conexión.'),
        ('Me detectan siempre. ¿Algún consejo?', 'Ve más lento, baja más hondo y usa el modo SILENCIO cuando te busquen. Bajo un témpano o bajo la capa de 100 m el sonar enemigo casi no te ve.'),
    ], '{up}depth40/support/', '/depth40/support/', 'PREGUNTAS FRECUENTES'),
    'en': ('depth40/support', 'Support', "Write to us and we'll get back to you as soon as possible. If it's a bug, tell us your phone model, the mission and what you were doing.", [
        ('How do I change the language?', 'On the main menu, tap SETTINGS and choose ENGLISH or ESPAÑOL.'),
        ("I can't hear anything.", "Check that your phone isn't on silent and that music and effects are on in SETTINGS. Sound starts with your first tap on the screen."),
        ('How do I see the tutorial again?', 'In SETTINGS, tap “View tutorial”. Each mission briefing also has a VIEW TUTORIAL button.'),
        ('I lost my progress.', 'Progress is saved only on your phone. If you uninstall the game or clear its data, it is lost. “Reset progress” in SETTINGS also erases it.'),
        ('What is free and what do I pay for?', 'Missions 1 and 2 and the tutorial are free. Missions 3 to 8 are unlocked with a one-time payment, with no ads or subscriptions.'),
        ('I paid and the missions are still locked.', 'Open the game with an internet connection, go to MISSIONS › UNLOCK and tap RESTORE PURCHASE. Use the same Google account you bought it with. If the payment was pending, it will open once the store confirms it.'),
        ('Do I need an internet connection?', 'Only to buy or restore the purchase. Depth 40 plays fully offline.'),
        ('I keep getting detected. Any tips?', 'Go slower, dive deeper and use SILENT mode when they hunt you. Under an ice floe or below the 100 m layer, enemy sonar can barely see you.'),
    ], '{up}depth40/soporte/', '/depth40/soporte/', 'FREQUENTLY ASKED QUESTIONS'),
}
for lang, (path, h1, lead, faq, alt, alt_abs, faq_h) in SUP.items():
    dl = ''.join(f'<dt>{q}</dt><dd>{a}</dd>' for q, a in faq)
    body = game_bar(lang, alt) + f'''
<main id="main" class="wrap doc">
  <h1>{h1.upper()} · DEPTH 40</h1>
  <p>{lead}</p>
  <p><a class="mail" href="mailto:{MAIL}?subject=Depth%2040">{MAIL}</a></p>
  <h2>{faq_h}</h2>
  <dl>{dl}</dl>
</main>
''' + game_footer(lang)
    page(path, lang, f'{h1} · Depth 40', f'{h1} · Depth 40 · Estudio Treso', 'game', body, alt_abs, 2)

# ================================================================ TRESO: Widget Design
WD_STYLES = [('terminal', 'Terminal', 'Terminal'), ('pixel', 'Pixel', 'Pixel'), ('hardware', 'Hardware', 'Hardware'),
             ('radio', 'Radio LCD', 'Radio LCD'), ('lab', 'Laboratorio', 'Lab'), ('crt', 'CRT Violeta', 'CRT Violet'),
             ('escritorio', 'Escritorio 95', 'Desktop 95'), ('mecha', 'Mecha', 'Mecha')]
WD = {
    'es': dict(
        tag='WIDGETS PARA TU PANTALLA DE INICIO',
        intro=['Ocho estilos de widgets pensados como un kit: cuatro piezas que calzan entre sí y llenan tu pantalla de inicio con la hora, el clima, la batería, tu agenda, tus pasos y más.',
               'Elige qué dato va en cada espacio, cambia los colores y mira cada estilo en pantalla completa antes de comprarlo.'],
        pills=['8 ESTILOS', 'TERMINAL GRATIS', 'PAGO ÚNICO', 'SIN SUSCRIPCIÓN', 'SIN ANUNCIOS', 'ESPAÑOL · ENGLISH'],
        shots_h='LOS 8 ESTILOS', feat_h='CÓMO FUNCIONA',
        feats=[('Un kit de 4 piezas', 'Un reloj ancho, dos piezas chicas y una grande. Juntas arman la pantalla completa.'),
               ('Tú eliges los datos', 'Hora, clima, batería, agenda, pasos, cuenta regresiva, otra ciudad, una nota tuya y más.'),
               ('Colores', 'Cada estilo trae varios colores para combinar con tu fondo de pantalla.'),
               ('Pruébalo antes', 'Mira cada estilo a tamaño real con tus propios datos antes de comprarlo.')],
        price_h='PRECIOS', prices=[('Terminal', 'Gratis'), ('Cada estilo', 'US$0,99'), ('Pack 1 · los 7 estilos', 'US$4,99'), ('Si ya compraste alguno', 'El Pack 1 lo descuenta')],
        price_note='Pago único con tu cuenta de Google Play o App Store. Precios de referencia en dólares; la tienda los muestra en tu moneda.',
        alt='Capturas de TRESO: Widget Design',
        desc='TRESO: Widget Design: ocho estilos de widgets para Android y iPhone. Una app de Estudio Treso.'),
    'en': dict(
        tag='WIDGETS FOR YOUR HOME SCREEN',
        intro=['Eight widget styles designed as a kit: four pieces that fit together and fill your Home Screen with the time, weather, battery, calendar, steps and more.',
               'Choose what goes in each spot, change the colors and see every style full screen before you buy it.'],
        pills=['8 STYLES', 'TERMINAL IS FREE', 'ONE-TIME PURCHASE', 'NO SUBSCRIPTION', 'NO ADS', 'ENGLISH · ESPAÑOL'],
        shots_h='THE 8 STYLES', feat_h='HOW IT WORKS',
        feats=[('A 4-piece kit', 'A wide clock, two small pieces and a large one. Together they fill the screen.'),
               ('You choose the data', 'Time, weather, battery, calendar, steps, countdown, world clock, your own note and more.'),
               ('Colors', 'Every style comes in several colors to match your wallpaper.'),
               ('Try it first', 'See every style at full size with your own data before you buy it.')],
        price_h='PRICES', prices=[('Terminal', 'Free'), ('Each style', 'US$0.99'), ('Pack 1 · all 7 styles', 'US$4.99'), ('Already bought some?', 'Pack 1 takes them off')],
        price_note='One-time payment with your Google Play or App Store account. Reference prices in US dollars; the store shows them in your currency.',
        alt='TRESO: Widget Design screenshots',
        desc='TRESO: Widget Design: eight widget styles for Android and iPhone. An app by Estudio Treso.'),
}
for lang, t in WD.items():
    path = 'widgetdesign' if lang == 'es' else 'widgetdesign/en'
    alt = '{up}widgetdesign/en/' if lang == 'es' else '{up}widgetdesign/'
    shots = ''.join(f'<figure><img src="{{up}}assets/wd-{k}-{lang}.jpg" width="540" height="1080" loading="lazy" alt="{es if lang == "es" else en}"><figcaption>{(es if lang == "es" else en).upper()}</figcaption></figure>'
                    for k, es, en in WD_STYLES)
    feats = ''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in t['feats'])
    prices = ''.join(f'<div><b>{b}</b><span>{a}</span></div>' for a, b in t['prices'])
    pills = ''.join(f'<span class="pill">{p}</span>' for p in t['pills'])
    body = game_bar(lang, alt) + f'''
<main id="main" class="wrap">
  <div class="hero" style="background-image:url('{{up}}assets/wd-hero-{lang}.jpg')" role="img" aria-label="TRESO: Widget Design"></div>
  <h1>WIDGET <em>DESIGN</em></h1>
  <p class="tag">{t['tag']}</p>
  {''.join(f'<p class="intro">{p}</p>' for p in t['intro'])}
  {store_buttons('widgetdesign', lang)}
  <div class="pills">{pills}</div>
  <h2>{t['shots_h']}</h2>
  <div class="shots" role="group" aria-label="{t['alt']}" tabindex="0">{shots}</div>
  <h2>{t['feat_h']}</h2>
  <div class="feat">{feats}</div>
  <h2>{t['price_h']}</h2>
  <div class="feat prices">{prices}</div>
  <p class="note">{t['price_note']}</p>
</main>
''' + game_footer(lang, 'widgetdesign')
    page(path, lang, 'TRESO: Widget Design · Estudio Treso', t['desc'], 'game wd', body, '/widgetdesign/en/' if lang == 'es' else '/widgetdesign/', 1 if lang == 'es' else 2, og='wd-hero')

WD_PRIV = {
    'es': ('widgetdesign/privacidad', 'Política de privacidad', f'Última actualización: {UPDATED_WD["es"]}', [
        ('', 'TRESO: Widget Design es una app desarrollada por Estudio Treso, marca de TRESO SPA (Santiago, Chile).'),
        ('Datos que recopilamos', 'Ninguno. La app no pide registro, no tiene cuentas propias, no muestra publicidad, no usa servicios de análisis y no nos envía información. No tenemos servidores que reciban tus datos.'),
        ('Datos que la app lee en tu teléfono', 'Para mostrarlos en tus widgets, la app lee en tu propio teléfono la hora, la fecha, la batería y el espacio libre (sin pedir permiso). Solo si tú das el permiso, también lee: tu calendario (los eventos de hoy y de los próximos 7 días; en iPhone también tus recordatorios), tu actividad (pasos; en iPhone también distancia, pisos y horas de sueño desde Salud) y tu ubicación aproximada. Todo se procesa dentro del teléfono y no lo recibimos.'),
        ('Clima y ubicación', 'Para el clima, la app usa tu ubicación aproximada. En Android, la ubicación se redondea a cerca de 1 km y se envía al Instituto Meteorológico de Noruega (MET Norway, api.met.no) para obtener el pronóstico; no se envía ningún otro dato. Los datos del clima son de MET Norway, con licencia CC BY 4.0. En iPhone, el clima lo entrega Apple Weather, según la política de privacidad de Apple. La hora del atardecer se calcula dentro del teléfono.'),
        ('Compras dentro de la app', 'El estilo Terminal es gratis. Los demás estilos y el Pack 1 se compran con un pago único. El pago lo procesa la tienda (Google Play o App Store) con tu cuenta de esa tienda, según su propia política de privacidad. Nosotros no recibimos tus datos de pago: la app solo le pregunta a la tienda qué compraste para desbloquear tus estilos.'),
        ('Datos guardados en tu dispositivo', 'La app guarda en tu teléfono tus ajustes (idioma, formato de hora, colores, datos elegidos para cada pieza), tu nota, tu cuenta regresiva y los últimos datos leídos para que los widgets se vean al instante. Nada de eso sale del dispositivo y se borra al desinstalar la app.'),
        ('Permisos', 'Cada permiso es opcional: si no lo das, ese dato aparece como «sin permiso» y todo lo demás funciona igual. Puedes quitarlos cuando quieras en los ajustes de tu teléfono.'),
        ('Niños', 'La app no está dirigida a menores de 13 años y no recopila datos de nadie.'),
        ('Cambios', 'Si esta política cambia, publicaremos la nueva versión en esta misma página con su fecha.'),
        ('Contacto', f'Para cualquier consulta sobre privacidad escríbenos a <a class="mail" href="mailto:{MAIL}">{MAIL}</a>'),
    ], '/widgetdesign/privacy/'),
    'en': ('widgetdesign/privacy', 'Privacy Policy', f'Last updated: {UPDATED_WD["en"]}', [
        ('', 'TRESO: Widget Design is an app developed by Estudio Treso, a brand of TRESO SPA (Santiago, Chile).'),
        ('Data we collect', 'None. The app requires no sign-up, has no accounts of its own, shows no ads, uses no analytics services and sends no information to us. We have no servers that receive your data.'),
        ('Data the app reads on your phone', 'To show it in your widgets, the app reads on your own phone the time, date, battery and free storage (no permission needed). Only if you grant permission, it also reads: your calendar (events for today and the next 7 days; on iPhone also your reminders), your activity (steps; on iPhone also distance, floors and sleep hours from Health) and your approximate location. Everything is processed on the phone and we never receive it.'),
        ('Weather and location', 'For the weather, the app uses your approximate location. On Android, the location is rounded to about 1 km and sent to the Norwegian Meteorological Institute (MET Norway, api.met.no) to get the forecast; no other data is sent. Weather data is from MET Norway, licensed under CC BY 4.0. On iPhone, weather is provided by Apple Weather, under Apple’s privacy policy. Sunset time is calculated on the phone.'),
        ('In-app purchases', 'The Terminal style is free. The other styles and Pack 1 are one-time purchases. Payment is processed by the store (Google Play or the App Store) with your store account, under the store’s own privacy policy. We never receive your payment details: the app only asks the store what you bought in order to unlock your styles.'),
        ('Data stored on your device', 'The app stores on your phone your settings (language, time format, colors, the data chosen for each piece), your note, your countdown and the latest data read so widgets show up instantly. None of it leaves the device, and it is deleted when you uninstall the app.'),
        ('Permissions', 'Every permission is optional: if you don’t grant it, that item shows as “no permission” and everything else works the same. You can remove them at any time in your phone settings.'),
        ('Children', 'The app is not directed at children under 13 and collects no data from anyone.'),
        ('Changes', 'If this policy changes, we will publish the new version on this same page with its date.'),
        ('Contact', f'For any privacy question, write to us at <a class="mail" href="mailto:{MAIL}">{MAIL}</a>'),
    ], '/widgetdesign/privacidad/'),
}


def doc_page(slug, lang, path, h1, meta, secs, alt_abs, klass, og):
    name = PRODUCT_NAME[slug]
    body_secs = ''.join((f'<h2>{h.upper()}</h2>' if h else '') + f'<p>{p}</p>' for h, p in secs)
    body = game_bar(lang, '{up}' + alt_abs.lstrip('/')) + f'''
<main id="main" class="wrap doc">
  <h1>{h1.upper()}</h1>
  <p class="meta">{name} · {meta}</p>
  {body_secs}
</main>
''' + game_footer(lang, slug)
    page(path, lang, f'{h1} · {name}', f'{h1} · {name} · Estudio Treso', klass, body, alt_abs, 2, og=og)


for lang, (path, h1, meta, secs, alt_abs) in WD_PRIV.items():
    doc_page('widgetdesign', lang, path, h1, meta, secs, alt_abs, 'game wd', 'wd-hero')

WD_SUP = {
    'es': ('widgetdesign/soporte', 'Soporte', 'Escríbenos y te respondemos lo antes posible. Si es un error, cuéntanos el modelo de tu teléfono, el estilo y qué estabas haciendo.', [
        ('¿Cómo agrego los widgets en Android?', 'Mantén presionado un espacio vacío de tu pantalla de inicio, toca «Widgets» y busca TRESO. Arma el kit con «TRESO · Ancho» arriba, dos «TRESO · Cuadro» al medio y «TRESO · Grande» abajo. O usa «TRESO · Pantalla completa», que es el kit entero en un solo widget. Los widgets aparecen con el estilo que elegiste con «Usar estilo».'),
        ('¿Cómo agrego los widgets en iPhone?', 'Mantén presionada la pantalla de inicio, toca «Editar» › «Agregar widget» y busca TRESO. Agrega los cuatro tamaños del kit en el orden que muestra la app (pestaña Estilos › Usar estilo › Cómo agregarlo).'),
        ('¿Cómo cambio el estilo o la pieza de un widget?', 'Mantén presionado el widget. En Android toca «Configuración» (o el ícono de lápiz o engranaje); en iPhone toca «Editar widget». Ahí eliges el estilo y cuál de las 4 piezas muestra. Para cambiar todos a la vez, en la app toca «Usar estilo» en el estilo que quieras.'),
        ('El widget quedó en otra página (Android).', 'Algunos teléfonos, por ejemplo los Samsung, ponen el widget nuevo donde encuentran espacio y no siempre en la página que estabas mirando. Mantenlo presionado y arrástralo a la página que quieras.'),
        ('Dice «SIN PERMISO».', 'Ese dato necesita un permiso (calendario, ubicación o actividad). En Android, toca el widget y luego «Permitir». También puedes darlo en la app, en Ajustes › Permisos, o en los ajustes de tu teléfono.'),
        ('El clima no aparece.', 'El clima necesita el permiso de ubicación y conexión a internet. Se actualiza cada 30 minutos; abre la app una vez para que lo busque al tiro.'),
        ('¿Qué es gratis y qué se paga?', 'El estilo Terminal es gratis, con todas sus funciones. Cada uno de los otros 7 estilos cuesta US$0,99, o los 7 juntos con el Pack 1 por US$4,99. Si ya compraste algún estilo, el Pack 1 te sale más barato. Es un pago único, sin anuncios ni suscripciones.'),
        ('Ya pagué y el estilo sigue bloqueado.', 'Abre la app con internet y en Ajustes toca «Restaurar compras». Usa la misma cuenta de Google o Apple con la que compraste. Si el pago quedó pendiente, el estilo se abre cuando la tienda lo confirme.'),
        ('La hora del widget se atrasa unos segundos (Android).', 'Es normal: Android actualiza los widgets una vez por minuto y puede demorar algunos segundos en cambiar el número.'),
    ], '/widgetdesign/support/', 'PREGUNTAS FRECUENTES'),
    'en': ('widgetdesign/support', 'Support', "Write to us and we'll get back to you as soon as possible. If it's a bug, tell us your phone model, the style and what you were doing.", [
        ('How do I add the widgets on Android?', 'Press and hold an empty spot on your Home screen, tap “Widgets” and find TRESO. Build the kit with “TRESO · Wide” on top, two “TRESO · Square” in the middle and “TRESO · Large” below. Or use “TRESO · Full screen”, the whole kit in one widget. Widgets show the style you picked with “Use style”.'),
        ('How do I add the widgets on iPhone?', 'Press and hold the Home Screen, tap “Edit” › “Add Widget” and find TRESO. Add the four kit sizes in the order the app shows (Styles tab › Use style › How to add it).'),
        ('How do I change a widget’s style or piece?', 'Press and hold the widget. On Android tap “Settings” (or the pencil or gear icon); on iPhone tap “Edit Widget”. There you choose the style and which of the 4 pieces it shows. To change them all at once, tap “Use style” on the style you want in the app.'),
        ('The widget landed on another page (Android).', 'Some phones, Samsung for example, place a new widget wherever there is room, not always on the page you were looking at. Press and hold it and drag it to the page you want.'),
        ('It says “NO PERMISSION”.', 'That item needs a permission (calendar, location or activity). On Android, tap the widget and then “Allow”. You can also grant it in the app, under Settings › Permissions, or in your phone settings.'),
        ("The weather doesn't show up.", 'Weather needs the location permission and an internet connection. It refreshes every 30 minutes; open the app once to fetch it right away.'),
        ('What is free and what do I pay for?', 'The Terminal style is free, with every feature. Each of the other 7 styles is US$0.99, or all 7 together with Pack 1 for US$4.99. If you already bought a style, Pack 1 costs less. It is a one-time payment, with no ads or subscriptions.'),
        ('I paid and the style is still locked.', 'Open the app with an internet connection and tap “Restore purchases” in Settings. Use the same Google or Apple account you bought it with. If the payment was pending, the style unlocks once the store confirms it.'),
        ('The widget clock lags a few seconds (Android).', 'That is normal: Android refreshes widgets once a minute and may take a few seconds to change the number.'),
    ], '/widgetdesign/soporte/', 'FREQUENTLY ASKED QUESTIONS'),
}
for lang, (path, h1, lead, faq, alt_abs, faq_h) in WD_SUP.items():
    dl = ''.join(f'<dt>{q}</dt><dd>{a}</dd>' for q, a in faq)
    body = game_bar(lang, '{up}' + alt_abs.lstrip('/')) + f'''
<main id="main" class="wrap doc">
  <h1>{h1.upper()} · WIDGET DESIGN</h1>
  <p>{lead}</p>
  <p><a class="mail" href="mailto:{MAIL}?subject=TRESO%20Widget%20Design">{MAIL}</a></p>
  <h2>{faq_h}</h2>
  <dl>{dl}</dl>
</main>
''' + game_footer(lang, 'widgetdesign')
    page(path, lang, f'{h1} · Widget Design', f'{h1} · TRESO: Widget Design · Estudio Treso', 'game wd', body, alt_abs, 2, og='wd-hero')


# ================================================================ 12/12: Diario de cultivo
DD_SHOTS = [('inicio', 'Inicio', 'Welcome'), ('carpas', 'Mis carpas', 'My tents'), ('proyecto', 'Proyecto', 'Project'), ('bitacora', 'Bitácora', 'Logbook'),
            ('medidor', 'Medidor de luz', 'Light meter'), ('carpa', 'Tu carpa', 'Your tent'), ('informe', 'Informe', 'Report'), ('noche', 'Modo noche', 'Night mode')]
DD = {
    'es': dict(
        tag='DIARIO DE CULTIVO PARA CARPAS INDOOR',
        intro=['Lleva tu cultivo de interior día a día. Arma tu carpa con sus medidas, luces y plantas, y anota riegos, pH, EC, clima, podas y fotos en una bitácora ordenada por semana.',
               'La app calcula el avance del ciclo, te muestra cuánto falta para que se apague la luz, estima la cosecha y mide la luz con el sensor de tu teléfono. Al final te queda un informe con gráficos y fotos de todo el cultivo.'],
        pills=['PAGO ÚNICO', 'SIN ANUNCIOS', 'SIN SUSCRIPCIÓN', 'SIN CUENTA', 'FUNCIONA SIN INTERNET', 'ESPAÑOL · ENGLISH', '+18'],
        shots_h='CAPTURAS', feat_h='QUÉ HACE',
        feats=[('Tu carpa a escala', 'Medidas, sustrato, lámparas y plantas que mueves y ordenas como en tu carpa real.'),
               ('Bitácora', 'Riego con pH y EC, clima con VPD, luz, horario, etapa, podas, trasplantes, problemas y notas, con fotos.'),
               ('Reloj de luz', 'Horario 18/6, 12/12 o el tuyo, con la cuenta regresiva hasta que la luz se apaga. La app se pone oscura cuando tu carpa está a oscuras.'),
               ('Avance y cosecha', 'Porcentaje del ciclo, días en floración y fecha estimada de cosecha, que puedes ajustar.'),
               ('Medidor de luz', 'PPFD y DLI aproximados con el sensor del teléfono, según tu tipo de lámpara, con calibración.'),
               ('Recordatorios', 'Riego, revisión de plagas o lo que necesites, con aviso en el teléfono.'),
               ('Nutrientes', 'Tu lista de productos y dosis, a un toque en cada riego, con consejos generales por etapa.'),
               ('Informe final', 'Etapas, fechas clave, gráficos de pH, EC, clima y luz, y tus fotos. Para compartir o guardar.')],
        note='El medidor de luz es aproximado: un teléfono no reemplaza un medidor PAR profesional. Los rangos y consejos de la app son referencias generales. App para mayores de 18 años; respeta las leyes de tu país sobre cultivo.',
        alt='Capturas de 12/12', desc='12/12: diario de cultivo para carpas indoor, con bitácora, avance hasta la cosecha y medidor de luz. Para Android y iPhone. Una app de Estudio Treso.'),
    'en': dict(
        tag='GROW DIARY FOR INDOOR TENTS',
        intro=['Follow your indoor grow day by day. Set up your tent with its size, lights and plants, and log waterings, pH, EC, climate, training and photos in a logbook sorted by week.',
               'The app tracks cycle progress, shows how long until lights off, estimates harvest and measures light with your phone’s sensor. At the end you get a report with charts and photos of the whole grow.'],
        pills=['ONE-TIME PURCHASE', 'NO ADS', 'NO SUBSCRIPTION', 'NO ACCOUNT', 'WORKS OFFLINE', 'ENGLISH · ESPAÑOL', '18+'],
        shots_h='SCREENSHOTS', feat_h='WHAT IT DOES',
        feats=[('Your tent to scale', 'Size, medium, lamps and plants you move and arrange just like in your real tent.'),
               ('Logbook', 'Watering with pH and EC, climate with VPD, light, schedule, stage, training, transplants, issues and notes, with photos.'),
               ('Light clock', '18/6, 12/12 or your own schedule, with a countdown to lights off. The app goes dark when your tent does.'),
               ('Progress and harvest', 'Cycle percentage, days in flower and an estimated harvest date you can adjust.'),
               ('Light meter', 'Approximate PPFD and DLI from your phone’s sensor, by lamp type, with calibration.'),
               ('Reminders', 'Watering, pest checks or anything you need, with a notification on your phone.'),
               ('Nutrients', 'Your own list of products and doses, one tap on each watering, with general tips by stage.'),
               ('Final report', 'Stages, key dates, pH, EC, climate and light charts, and your photos. Ready to share or save.')],
        note='The light meter is approximate: a phone does not replace a professional PAR meter. The app’s ranges and tips are general references. For ages 18+; follow your country’s laws on growing.',
        alt='12/12 screenshots', desc='12/12: a grow diary for indoor tents, with a logbook, progress to harvest and a light meter. For Android and iPhone. An app by Estudio Treso.'),
}
for lang, t in DD.items():
    path = 'doce12' if lang == 'es' else 'doce12/en'
    alt = '{up}doce12/en/' if lang == 'es' else '{up}doce12/'
    shots = ''.join(f'<figure><img src="{{up}}assets/dd-{k}-{lang}.jpg" width="540" height="1080" loading="lazy" alt="{es if lang == "es" else en}"><figcaption>{(es if lang == "es" else en).upper()}</figcaption></figure>'
                    for k, es, en in DD_SHOTS)
    feats = ''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in t['feats'])
    pills = ''.join(f'<span class="pill">{p}</span>' for p in t['pills'])
    body = game_bar(lang, alt) + f"""
<main id="main" class="wrap">
  <div class="hero" style="background-image:url('{{up}}assets/dd-hero-{lang}.jpg')" role="img" aria-label="12/12"></div>
  <h1>12<em>/</em>12</h1>
  <p class="tag">{t['tag']}</p>
  {''.join(f'<p class="intro">{p}</p>' for p in t['intro'])}
  {store_buttons('doce12', lang)}
  <div class="pills">{pills}</div>
  <h2>{t['shots_h']}</h2>
  <div class="shots" role="group" aria-label="{t['alt']}" tabindex="0">{shots}</div>
  <h2>{t['feat_h']}</h2>
  <div class="feat">{feats}</div>
  <p class="note">{t['note']}</p>
</main>
""" + game_footer(lang, 'doce12')
    page(path, lang, '12/12: ' + ('Diario de cultivo' if lang == 'es' else 'Grow Diary') + ' · Estudio Treso', t['desc'], 'game dd', body, '/doce12/en/' if lang == 'es' else '/doce12/', 1 if lang == 'es' else 2, og='dd-hero')

DD_PRIV = {
    'es': ('doce12/privacidad', 'Política de privacidad', f'Última actualización: {UPDATED_DD["es"]}', [
        ('', '12/12: Diario de cultivo es una app desarrollada por Estudio Treso, marca de TRESO SPA (Santiago, Chile).'),
        ('Datos que recopilamos', 'Ninguno. La app no pide registro, no tiene cuentas, no muestra publicidad, no usa servicios de análisis y no nos envía información. Funciona sin internet y no tenemos servidores que reciban tus datos.'),
        ('Datos guardados en tu dispositivo', 'Todo lo que registras queda en el almacenamiento privado de la app en tu teléfono: tus proyectos (nombre, medidas, luces, plantas), la bitácora, los recordatorios, tu lista de nutrientes, tus ajustes, tu calibración del medidor y las fotos que agregues. Nada de eso sale del teléfono, salvo que tú compartas un informe. Se borra al desinstalar la app.'),
        ('Fotos', 'Cuando agregas una foto, la eliges tú con el selector del sistema o la cámara, y la app guarda una copia dentro de su propio espacio. La app no recorre ni lee el resto de tu galería.'),
        ('Sensor de luz y modelo del teléfono', 'El medidor lee el sensor de luz ambiental del teléfono solo mientras tienes abierta esa pantalla. La app también lee el modelo de tu teléfono y el nombre del sensor para aplicar una calibración de fábrica cuando existe para ese modelo. Todo se procesa en el teléfono y no lo recibimos.'),
        ('Notificaciones', 'Los recordatorios usan notificaciones locales, programadas en tu propio teléfono. El permiso es opcional: si no lo das, todo lo demás funciona igual. Puedes quitarlo cuando quieras en los ajustes de tu teléfono.'),
        ('Compartir un informe', 'Si decides compartir o guardar el informe de un cultivo, la app usa el menú de compartir de tu teléfono. Lo que envíes a otra app queda sujeto a la política de privacidad de esa app.'),
        ('Compra de la app', 'La compra la procesa la tienda (Google Play o App Store) con tu cuenta de esa tienda, según su propia política de privacidad. Nosotros no recibimos tus datos de pago.'),
        ('Edad', 'La app es para mayores de 18 años y no recopila datos de nadie.'),
        ('Cambios', 'Si esta política cambia, publicaremos la nueva versión en esta misma página con su fecha.'),
        ('Contacto', f'Para cualquier consulta sobre privacidad escríbenos a <a class="mail" href="mailto:{MAIL}">{MAIL}</a>'),
    ], '/doce12/privacy/'),
    'en': ('doce12/privacy', 'Privacy Policy', f'Last updated: {UPDATED_DD["en"]}', [
        ('', '12/12: Grow Diary is an app developed by Estudio Treso, a brand of TRESO SPA (Santiago, Chile).'),
        ('Data we collect', 'None. The app requires no sign-up, has no accounts, shows no ads, uses no analytics services and sends no information to us. It works offline and we have no servers that receive your data.'),
        ('Data stored on your device', 'Everything you log stays in the app’s private storage on your phone: your projects (name, size, lights, plants), the logbook, reminders, your nutrient list, your settings, your light meter calibration and the photos you add. None of it leaves the phone unless you share a report. It is deleted when you uninstall the app.'),
        ('Photos', 'When you add a photo, you pick it yourself with the system picker or the camera, and the app keeps a copy in its own storage. The app does not browse or read the rest of your gallery.'),
        ('Light sensor and phone model', 'The meter reads your phone’s ambient light sensor only while that screen is open. The app also reads your phone model and the sensor name to apply a factory calibration when one exists for that model. Everything is processed on the phone and we never receive it.'),
        ('Notifications', 'Reminders use local notifications scheduled on your own phone. The permission is optional: if you don’t grant it, everything else works the same. You can remove it at any time in your phone settings.'),
        ('Sharing a report', 'If you choose to share or save a grow report, the app uses your phone’s share menu. Whatever you send to another app is subject to that app’s privacy policy.'),
        ('App purchase', 'The purchase is processed by the store (Google Play or the App Store) with your store account, under the store’s own privacy policy. We never receive your payment details.'),
        ('Age', 'The app is intended for adults aged 18 and over and collects no data from anyone.'),
        ('Changes', 'If this policy changes, we will publish the new version on this same page with its date.'),
        ('Contact', f'For any privacy question, write to us at <a class="mail" href="mailto:{MAIL}">{MAIL}</a>'),
    ], '/doce12/privacidad/'),
}
for lang, (path, h1, meta, secs, alt_abs) in DD_PRIV.items():
    doc_page('doce12', lang, path, h1, meta, secs, alt_abs, 'game dd', 'dd-hero')

DD_SUP = {
    'es': ('doce12/soporte', 'Soporte', 'Escríbenos y te respondemos lo antes posible. Si es un error, cuéntanos el modelo de tu teléfono, la pantalla y qué estabas haciendo.', [
        ('¿Qué significa 12/12?', 'Es el horario de 12 horas de luz y 12 de oscuridad que se usa para que las plantas fotoperiódicas pasen a floración. Las automáticas florecen solas, sin cambiar el horario.'),
        ('¿Qué tan exacto es el medidor de luz?', 'Es aproximado. El teléfono mide lux y la app los convierte a PPFD según tu tipo de lámpara, y cada modelo de teléfono mide distinto. Para afinarlo, mide en el mismo punto con un medidor de verdad (o una app de referencia) y usa «Calibrar con otro medidor» en la pantalla Medir luz.'),
        ('¿Cómo mido bien?', 'Pon el teléfono horizontal, con la pantalla hacia la lámpara, a la altura de las puntas de las plantas, y déjalo quieto unos segundos. El sensor suele estar arriba de la pantalla, cerca de la cámara frontal: no lo tapes con el dedo. En Android no uses papel encima del sensor.'),
        ('Mi cultivo ya empezó. ¿Puedo agregarlo?', 'Sí. Al crear el proyecto elige «Ya empezó» y pon la fecha de inicio. Si ya está en 12/12, la app te pregunta desde cuándo para calcular el avance y la cosecha.'),
        ('¿Cómo paso a floración?', 'En el proyecto toca «Pasar a floración». También puedes registrar el cambio de horario a 12/12. La fecha estimada de cosecha se ajusta sola, y también puedes cambiarla a mano.'),
        ('¿Cómo muevo o edito las plantas?', 'En el proyecto, abre los ajustes del proyecto y toca «Editar proyecto». Los cambios quedan anotados en la bitácora.'),
        ('No me llegan los recordatorios.', 'Revisa que la app tenga permiso de notificaciones. Algunos teléfonos, por ejemplo los Samsung, detienen las apps para ahorrar batería: en los ajustes del teléfono, quita 12/12 de las apps suspendidas o del ahorro de batería.'),
        ('No puedo agregar fotos.', 'Actualiza la app a la última versión. Si sigue pasando, escríbenos con el modelo de tu teléfono.'),
        ('¿Dónde se guardan mis datos?', 'Solo en tu teléfono. Si desinstalas la app o borras sus datos, se pierden. Estamos preparando una opción de respaldo para una próxima versión.'),
        ('¿Cómo cambio el color o el idioma?', 'En Ajustes. En modo automático la app es clara cuando la luz de tu carpa está encendida y oscura cuando está apagada; también puedes dejarla siempre clara u oscura. El idioma se cambia con ES / EN arriba.'),
    ], '/doce12/support/', 'PREGUNTAS FRECUENTES'),
    'en': ('doce12/support', 'Support', "Write to us and we'll get back to you as soon as possible. If it's a bug, tell us your phone model, the screen and what you were doing.", [
        ('What does 12/12 mean?', 'It is the 12 hours on, 12 hours off light schedule used to switch photoperiod plants into flowering. Autoflowers bloom on their own, without changing the schedule.'),
        ('How accurate is the light meter?', 'It is approximate. The phone measures lux and the app converts it to PPFD by lamp type, and every phone model reads differently. To fine-tune it, measure at the same spot with a real meter (or a reference app) and use “Calibrate with another meter” on the Measure light screen.'),
        ('How do I measure properly?', 'Hold the phone flat, screen facing the lamp, at the height of the plant tops, and keep it still for a few seconds. The sensor is usually above the screen, near the front camera: don’t cover it with your finger. On Android, don’t put paper over the sensor.'),
        ('My grow has already started. Can I add it?', 'Yes. When creating the project choose “Already started” and enter the start date. If it is already on 12/12, the app asks since when so it can work out progress and harvest.'),
        ('How do I switch to flowering?', 'In the project tap “Switch to flowering”. You can also log the schedule change to 12/12. The estimated harvest date updates on its own, and you can also change it by hand.'),
        ('How do I move or edit plants?', 'In the project, open the project settings and tap “Edit project”. Changes are noted in the logbook.'),
        ("I don't get reminders.", 'Check that the app has notification permission. Some phones, Samsung for example, stop apps to save battery: in your phone settings, remove 12/12 from sleeping apps or battery saving.'),
        ("I can't add photos.", 'Update the app to the latest version. If it keeps happening, write to us with your phone model.'),
        ('Where is my data stored?', 'Only on your phone. If you uninstall the app or clear its data, it is lost. We are working on a backup option for an upcoming version.'),
        ('How do I change the color or the language?', 'In Settings. In automatic mode the app is light while your tent lights are on and dark while they are off; you can also keep it always light or dark. Switch the language with ES / EN at the top.'),
    ], '/doce12/soporte/', 'FREQUENTLY ASKED QUESTIONS'),
}
for lang, (path, h1, lead, faq, alt_abs, faq_h) in DD_SUP.items():
    dl = ''.join(f'<dt>{q}</dt><dd>{a}</dd>' for q, a in faq)
    body = game_bar(lang, '{up}' + alt_abs.lstrip('/')) + f"""
<main id="main" class="wrap doc">
  <h1>{h1.upper()} · 12/12</h1>
  <p>{lead}</p>
  <p><a class="mail" href="mailto:{MAIL}?subject=12%2F12">{MAIL}</a></p>
  <h2>{faq_h}</h2>
  <dl>{dl}</dl>
</main>
""" + game_footer(lang, 'doce12')
    page(path, lang, f'{h1} · 12/12', f'{h1} · 12/12 · Estudio Treso', 'game dd', body, alt_abs, 2, og='dd-hero')


# ================================================================ Términos del servicio (Depth 40 y Widget Design)
def terms(lang, name, what, buy, extra):
    if lang == 'es':
        return [
            ('', f'Estos términos rigen el uso de {name}, {what} desarrollada por Estudio Treso, marca de TRESO SPA (Santiago, Chile). Al descargar o usar la app aceptas estos términos.'),
            ('Licencia de uso', f'Te damos una licencia personal, no exclusiva e intransferible para usar {name} en tus dispositivos, según las reglas de la tienda donde la descargaste. No puedes copiar, modificar, revender, distribuir ni descompilar la app, salvo lo que la ley permita expresamente.'),
            ('Compras dentro de la app', buy + ' Los precios se muestran en la tienda, en tu moneda, antes de pagar. Las compras son de pago único, sin suscripción, y quedan asociadas a tu cuenta de la tienda: puedes recuperarlas con «Restaurar compras» usando la misma cuenta.'),
            ('Pagos y reembolsos', 'Los pagos los procesa Google Play o la App Store. Los reembolsos se rigen por las políticas de esa tienda; si tienes un problema con una compra, escríbenos y te ayudamos.'),
        ] + extra + [
            ('Actualizaciones y disponibilidad', 'Podemos actualizar la app para corregir errores, mejorarla o adaptarla a nuevas versiones del sistema. Hacemos lo posible para que funcione bien, pero no podemos garantizar que funcione en todos los modelos de teléfono ni sin interrupciones.'),
            ('Garantía y responsabilidad', 'En la medida que lo permita la ley, la app se entrega «tal cual», y TRESO SPA no responde por daños indirectos derivados de su uso. Nada en estos términos limita los derechos que te da la ley de protección al consumidor que te corresponda (en Chile, la Ley N° 19.496).'),
            ('Propiedad intelectual', f'{name}, su diseño, textos, gráficos y sonidos pertenecen a TRESO SPA o a sus licenciantes. Las tipografías usadas tienen licencia SIL Open Font License.'),
            ('Privacidad', 'El tratamiento de datos se explica en la política de privacidad de la app, publicada en este mismo sitio.'),
            ('Ley aplicable', 'Estos términos se rigen por las leyes de Chile, sin perjuicio de las normas de protección al consumidor de tu país de residencia que te sean aplicables.'),
            ('Cambios', 'Si estos términos cambian, publicaremos la nueva versión en esta misma página con su fecha.'),
            ('Contacto', f'TRESO SPA · Santiago, Chile · <a class="mail" href="mailto:{MAIL}">{MAIL}</a>'),
        ]
    return [
        ('', f'These terms govern your use of {name}, {what} developed by Estudio Treso, a brand of TRESO SPA (Santiago, Chile). By downloading or using the app you accept these terms.'),
        ('License', f'We grant you a personal, non-exclusive, non-transferable license to use {name} on your devices, under the rules of the store you downloaded it from. You may not copy, modify, resell, distribute or decompile the app, except as expressly permitted by law.'),
        ('In-app purchases', buy + ' Prices are shown in the store, in your currency, before you pay. Purchases are one-time payments, with no subscription, and are tied to your store account: you can recover them with “Restore purchases” using the same account.'),
        ('Payments and refunds', 'Payments are processed by Google Play or the App Store. Refunds are governed by that store’s policies; if you have a problem with a purchase, write to us and we will help.'),
    ] + extra + [
        ('Updates and availability', 'We may update the app to fix bugs, improve it or adapt it to new system versions. We do our best to make it work well, but we cannot guarantee it works on every phone model or without interruption.'),
        ('Warranty and liability', 'To the extent permitted by law, the app is provided “as is”, and TRESO SPA is not liable for indirect damages arising from its use. Nothing in these terms limits the rights you have under the consumer protection law that applies to you.'),
        ('Intellectual property', f'{name}, its design, text, graphics and sounds belong to TRESO SPA or its licensors. The typefaces used are licensed under the SIL Open Font License.'),
        ('Privacy', 'How data is handled is explained in the app’s privacy policy, published on this same site.'),
        ('Governing law', 'These terms are governed by the laws of Chile, without prejudice to the consumer protection rules of your country of residence that apply to you.'),
        ('Changes', 'If these terms change, we will publish the new version on this same page with its date.'),
        ('Contact', f'TRESO SPA · Santiago, Chile · <a class="mail" href="mailto:{MAIL}">{MAIL}</a>'),
    ]


TERMS = [
    ('widgetdesign', 'game wd', 'wd-hero', 'TRESO: Widget Design',
     {'es': 'una app de widgets', 'en': 'a widget app'},
     {'es': 'El estilo Terminal es gratis. Los demás estilos y el Pack 1 se desbloquean con compras dentro de la app.',
      'en': 'The Terminal style is free. The other styles and Pack 1 are unlocked with in-app purchases.'},
     {'es': [('Datos de terceros', 'El clima viene de servicios externos (MET Norway en Android, con licencia CC BY 4.0, y Apple Weather en iPhone) y puede no ser exacto. Los datos de los widgets son informativos.')],
      'en': [('Third-party data', 'Weather comes from external services (MET Norway on Android, licensed under CC BY 4.0, and Apple Weather on iPhone) and may not be accurate. Widget data is for information only.')]}),
    ('depth40', 'game', 'd40-hero', 'Depth 40',
     {'es': 'un juego', 'en': 'a game'},
     {'es': 'Las misiones 1 y 2 son gratis. Las misiones 3 a 8 se desbloquean con una compra dentro de la app.',
      'en': 'Missions 1 and 2 are free. Missions 3 to 8 are unlocked with an in-app purchase.'},
     {'es': [], 'en': []}),
]
for slug, klass, og, name, what, buy, extra in TERMS:
    for lang in ('es', 'en'):
        path = f'{slug}/terminos' if lang == 'es' else f'{slug}/terms'
        alt_abs = f'/{slug}/terms/' if lang == 'es' else f'/{slug}/terminos/'
        upd = UPDATED_WD[lang]
        doc_page(slug, lang, path, 'Términos del servicio' if lang == 'es' else 'Terms of Service',
                 ('Última actualización: ' if lang == 'es' else 'Last updated: ') + upd,
                 terms(lang, name, what[lang], buy[lang], extra[lang]), alt_abs, klass, og)


# 12/12 es una app pagada (sin compras dentro de la app): se cambian esas dos secciones de los términos generales.
DD_TERMS_BUY = {
    'es': [('Compra de la app', '12/12 se compra con un pago único en la tienda (Google Play o App Store). No tiene compras dentro de la app, anuncios ni suscripción. El precio se muestra en la tienda, en tu moneda, antes de pagar. La compra queda asociada a tu cuenta de la tienda: puedes volver a instalar la app sin pagar de nuevo usando la misma cuenta.'),
           ('Pagos y reembolsos', 'Los pagos los procesa Google Play o la App Store. Los reembolsos se rigen por las políticas de esa tienda; si tienes un problema con tu compra, escríbenos y te ayudamos.')],
    'en': [('App purchase', '12/12 is bought with a one-time payment in the store (Google Play or the App Store). It has no in-app purchases, ads or subscription. The price is shown in the store, in your currency, before you pay. The purchase is tied to your store account: you can reinstall the app without paying again using the same account.'),
           ('Payments and refunds', 'Payments are processed by Google Play or the App Store. Refunds are governed by that store’s policies; if you have a problem with your purchase, write to us and we will help.')],
}
DD_TERMS_EXTRA = {
    'es': [('Mayoría de edad y uso responsable', 'La app es para mayores de 18 años. Es una herramienta para llevar el registro de tu propio cultivo de plantas; no promueve ni facilita actividades ilegales. Eres responsable de cumplir las leyes de tu país sobre el cultivo.'),
           ('Información de referencia', 'Las mediciones de luz son aproximadas y dependen del sensor de cada teléfono. Los rangos, fechas estimadas y consejos de la app son referencias generales: no reemplazan un instrumento profesional, el consejo de un experto ni las instrucciones de los fabricantes de tus productos.'),
           ('Tus registros', 'Tus registros y fotos se guardan solo en tu teléfono. No tenemos copia de ellos y no podemos recuperarlos si se pierden.'),
           ('Códigos promocionales', 'Podemos entregar códigos para descargar 12/12 sin costo, por ejemplo a través de tiendas de cultivo. Cada código es de un solo uso, solo para mayores de 18 años y se canjea en Google Play con una cuenta de un país donde la app esté disponible. Los códigos no tienen valor en dinero, no se pueden vender ni cambiar por dinero, y vencen en la fecha indicada en la promoción. Un código ya canjeado, vencido o perdido no se puede reponer. El canje se rige además por los términos de Google Play. Podemos cancelar los códigos si se usan en contra de estas condiciones.')],
    'en': [('Age and responsible use', 'The app is intended for adults aged 18 and over. It is a tool to keep a record of your own plant grow; it does not promote or facilitate illegal activity. You are responsible for complying with your country’s laws on growing.'),
           ('Reference information', 'Light readings are approximate and depend on each phone’s sensor. The app’s ranges, estimated dates and tips are general references: they do not replace a professional instrument, expert advice or the instructions from the makers of your products.'),
           ('Your records', 'Your records and photos are stored only on your phone. We keep no copy of them and cannot recover them if they are lost.'),
           ('Promotional codes', 'We may hand out codes to download 12/12 at no cost, for example through grow shops. Each code is single-use, for adults aged 18 and over only, and is redeemed on Google Play with an account from a country where the app is available. Codes have no cash value, cannot be sold or exchanged for money, and expire on the date set for the promotion. A code that has been redeemed, has expired or has been lost cannot be replaced. Redemption is also governed by Google Play’s terms. We may cancel codes that are used against these conditions.')],
}
for lang in ('es', 'en'):
    secs = terms(lang, '12/12', 'una app de registro de cultivo' if lang == 'es' else 'a grow-logging app', '', DD_TERMS_EXTRA[lang])
    secs[2:4] = DD_TERMS_BUY[lang]
    doc_page('doce12', lang, 'doce12/terminos' if lang == 'es' else 'doce12/terms', 'Términos del servicio' if lang == 'es' else 'Terms of Service',
             ('Última actualización: ' if lang == 'es' else 'Last updated: ') + UPDATED_DD[lang], secs,
             '/doce12/terms/' if lang == 'es' else '/doce12/terminos/', 'game dd', 'dd-hero')


# ================================================================ My Kardek: fichero de notas
# Blanco, tinta negra, letra JetBrains Mono y el amarillo de las etiquetas, como la app.
MK_SHOTS = [('inicio', 'El fichero', 'The card file'), ('cajon', 'Un cajón lleno', 'A full drawer'), ('plantillas', 'Elegir plantilla', 'Pick a template'),
            ('nota', 'No olvidar', 'Note to self'), ('fotos', 'Seguimiento con fotos', 'Photo tracker'), ('cotizacion', 'Cotización', 'Quote'), ('presupuesto', 'Presupuesto de fiesta', 'Party budget'),
            ('hoja', 'Hoja de cuaderno', 'Notebook page'), ('receta', 'Receta', 'Recipe'), ('semana', 'Mi semana', 'My week'),
            ('decision', 'A decidir', 'Decision'), ('buscar', 'Buscar', 'Search'), ('clave', 'Cajón con clave', 'Locked drawer')]
MK_FAMS = [('A', 'Hojas', 'Pages', 1), ('B', 'Notas rápidas', 'Quick notes', 4), ('C', 'Listas y tareas', 'Lists & tasks', 8), ('D', 'Planificadores', 'Planners', 6),
           ('E', 'Seguimiento', 'Trackers', 7), ('F', 'Decisiones', 'Decisions', 3), ('G', 'Cómo me siento', 'How I feel', 5),
           ('H', 'Recados', 'Notes for others', 7), ('I', 'Recetas', 'Recipes', 1), ('J', 'Cotizaciones', 'Quotes', 3), ('K', 'Presupuestos', 'Budgets', 3)]
MK = {
    'es': dict(
        tag='TU FICHERO DE NOTAS',
        intro=['Un fichero de verdad en tu teléfono: cuatro cajones que abres y cierras, y fichas que sacas, escribes y vuelves a guardar.',
               'Parte con una hoja de cuaderno en blanco o elige entre 48 plantillas: listas, planificadores, seguimientos con fotos, recetas, recados, cotizaciones y presupuestos. Todo se edita, todo queda en tu teléfono y funciona sin internet.',
               'La app es gratis con cuatro plantillas: la hoja de cuaderno (líneas, cuadrícula, puntos o en blanco), No olvidar, ¿Qué estoy haciendo? y Mi semana. Las otras 44 se desbloquean con un solo pago, para siempre.'],
        pills=['GRATIS', 'SIN ANUNCIOS', 'SIN SUSCRIPCIÓN', 'SIN CUENTA', 'FUNCIONA SIN INTERNET', '48 PLANTILLAS', 'ESPAÑOL · ENGLISH'],
        shots_h='CAPTURAS', feat_h='QUÉ HACE', fam_h='LAS 48 PLANTILLAS',
        feats=[('4 cajones', 'Ponle nombre y color de etiqueta a cada uno. Las fichas se ordenan solas por nombre.'),
               ('48 plantillas', 'Cuatro gratis y 44 más con un pago único, en 11 familias. Cada título, casilla y opción se edita.'),
               ('Seguimiento con fotos', 'Una planta que crece, una obra, tus hijos: foto, fecha y nota, una tras otra.'),
               ('Cotizaciones al paso', 'Tu logo, de quién es, el cliente y los ítems. Sin cálculos automáticos: tú escribes valores e impuestos.'),
               ('Presupuestos', 'Una fiesta, un viaje o el mes: anota lo que gastas, marca lo pagado y lleva el total.'),
               ('Cajón con clave', 'Protege cualquier cajón con una clave de 4 dígitos.'),
               ('Buscar', 'Encuentra cualquier ficha por lo que escribiste en ella.'),
               ('JPG o PDF', 'Envía una ficha por WhatsApp o correo, o guárdala en tu teléfono, de borde a borde.')],
        note='Las cotizaciones de My Kardek son un borrador rápido para mandar a un cliente: no son boleta ni factura. Ni las cotizaciones ni los presupuestos hacen cálculos: tú escribes los montos.',
        alt='Capturas de My Kardek', desc='My Kardek: un fichero de notas con cuatro cajones y 48 plantillas, sin internet. Para Android y iPhone. Una app de Estudio Treso.'),
    'en': dict(
        tag='YOUR NOTE CARD FILE',
        intro=['A real card file on your phone: four drawers you open and close, and cards you take out, write on and put back.',
               'Start with a blank notebook page or pick one of 48 templates: lists, planners, photo trackers, recipes, notes for others, quotes and budgets. Everything is editable, everything stays on your phone and it works offline.',
               'The app is free with four templates: the notebook page (lines, grid, dots or blank), Note to self, What am I even doing? and My week. The other 44 unlock with a single payment, forever.'],
        pills=['FREE', 'NO ADS', 'NO SUBSCRIPTION', 'NO ACCOUNT', 'WORKS OFFLINE', '48 TEMPLATES', 'ENGLISH · ESPAÑOL'],
        shots_h='SCREENSHOTS', feat_h='WHAT IT DOES', fam_h='THE 48 TEMPLATES',
        feats=[('4 drawers', 'Give each one a name and a label color. Cards sort themselves by name.'),
               ('48 templates', 'Four free and 44 more with a one-time payment, in 11 families. Every title, box and option is editable.'),
               ('Photo trackers', 'A growing plant, a building project, your kids: photo, date and note, one after another.'),
               ('Quick quotes', 'Your logo, who it’s from, the client and the items. No automatic math: you type your own amounts and taxes.'),
               ('Budgets', 'A party, a trip or the month: jot down what you spend, tick what’s paid and keep the total.'),
               ('Locked drawer', 'Protect any drawer with a 4-digit code.'),
               ('Search', 'Find any card by what you wrote on it.'),
               ('JPG or PDF', 'Send a card by WhatsApp or email, or save it to your phone, edge to edge.')],
        note='My Kardek quotes are a quick draft to send to a client: they are not invoices or tax documents. Neither quotes nor budgets do any math: you type the amounts.',
        alt='My Kardek screenshots', desc='My Kardek: a note card file with four drawers and 48 templates, works offline. For Android and iPhone. An app by Estudio Treso.'),
}
for lang, t in MK.items():
    path = 'kardek' if lang == 'es' else 'kardek/en'
    alt = '{up}kardek/en/' if lang == 'es' else '{up}kardek/'
    shots = ''.join(f'<figure><img src="{{up}}assets/mk-{k}-{lang}.jpg" width="540" height="1080" loading="lazy" alt="{es if lang == "es" else en}"><figcaption>{(es if lang == "es" else en).upper()}</figcaption></figure>'
                    for k, es, en in MK_SHOTS)
    feats = ''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in t['feats'])
    fams = ''.join(f'<li data-l="{l}">{(es if lang == "es" else en).upper()}<span>{n}</span></li>' for l, es, en, n in MK_FAMS)
    pills = ''.join(f'<span class="pill">{p}</span>' for p in t['pills'])
    body = game_bar(lang, alt) + f"""
<main id="main" class="wrap">
  <div class="hero" style="background-image:url('{{up}}assets/mk-hero-{lang}.jpg')" role="img" aria-label="My Kardek"></div>
  <h1><span>MY KARDEK</span></h1>
  <p class="tag">{t['tag']}</p>
  {''.join(f'<p class="intro">{p}</p>' for p in t['intro'])}
  {store_buttons('kardek', lang)}
  <div class="pills">{pills}</div>
  <h2>{t['shots_h']}</h2>
  <div class="shots" role="group" aria-label="{t['alt']}" tabindex="0">{shots}</div>
  <h2>{t['feat_h']}</h2>
  <div class="feat">{feats}</div>
  <h2>{t['fam_h']}</h2>
  <ol class="missions fams">{fams}</ol>
  <p class="note">{t['note']}</p>
</main>
""" + game_footer(lang, 'kardek')
    page(path, lang, 'My Kardek · Estudio Treso', t['desc'], 'game mk', body, '/kardek/en/' if lang == 'es' else '/kardek/', 1 if lang == 'es' else 2, og='mk-hero')

MK_PRIV = {
    'es': ('kardek/privacidad', 'Política de privacidad', f'Última actualización: {UPDATED_MK["es"]}', [
        ('', 'My Kardek es una app desarrollada por Estudio Treso, marca de TRESO SPA (Santiago, Chile).'),
        ('Datos que recopilamos', 'Ninguno. La app no pide registro, no tiene cuentas, no muestra publicidad, no usa servicios de análisis y no nos envía información. Funciona sin internet y no tenemos servidores que reciban tus datos.'),
        ('Datos guardados en tu dispositivo', 'Todo lo que escribes queda en el almacenamiento privado de la app en tu teléfono: tus fichas y su contenido, los nombres y colores de tus cajones, tus ajustes (idioma y sonidos) y las fotos que agregues. Nada de eso sale del teléfono, salvo que tú envíes o guardes una ficha como imagen. Se borra al desinstalar la app.'),
        ('Fotos', 'Cuando agregas una foto a una ficha (por ejemplo, en un seguimiento o el logo de una cotización), la eliges tú con la cámara o el selector del sistema, y la app guarda una copia dentro de su propio espacio. La app no recorre ni lee el resto de tu galería. El permiso de cámara se pide solo cuando tú tocas para tomar una foto.'),
        ('Clave de los cajones', 'Si proteges un cajón con una clave de 4 dígitos, la app no guarda la clave: guarda en tu teléfono solo una huella de ella para poder comprobarla. La clave impide abrir el cajón desde la app, pero no cifra su contenido. Si la olvidas no se puede recuperar; la única forma de quitarla es vaciar ese cajón.'),
        ('Enviar o guardar una ficha', 'Cuando tocas ENVIAR, la app crea la imagen (JPG) o el PDF de la ficha dentro de tu teléfono. Si eliges enviarla, se abre el menú de compartir del sistema y tú decides a quién y por dónde; lo que envíes a otra app queda sujeto a la política de privacidad de esa app. Si eliges guardarla, en Android la imagen queda en tu galería (Imágenes › My Kardek) y el PDF en Descargas › My Kardek; en iPhone se abre el menú del sistema, donde eliges «Guardar imagen» o «Guardar en Archivos».'),
        ('Sonidos y vibración', 'Se usan solo como efectos al abrir y cerrar cajones y fichas. Los sonidos se apagan en Ajustes.'),
        ('Compras dentro de la app', 'La app es gratis. Si desbloqueas las plantillas, el pago lo procesa la tienda (Google Play o App Store) con tu cuenta de esa tienda, según su propia política de privacidad. La app solo le pregunta a la tienda si la compra existe, para desbloquear las plantillas; nosotros no recibimos tus datos de pago ni personales.'),
        ('Niños', 'La app no está dirigida a menores de 13 años y no recopila datos de nadie.'),
        ('Cambios', 'Si esta política cambia, publicaremos la nueva versión en esta misma página con su fecha.'),
        ('Contacto', f'Para cualquier consulta sobre privacidad escríbenos a <a class="mail" href="mailto:{MAIL}">{MAIL}</a>'),
    ], '/kardek/privacy/'),
    'en': ('kardek/privacy', 'Privacy Policy', f'Last updated: {UPDATED_MK["en"]}', [
        ('', 'My Kardek is an app developed by Estudio Treso, a brand of TRESO SPA (Santiago, Chile).'),
        ('Data we collect', 'None. The app requires no sign-up, has no accounts, shows no ads, uses no analytics services and sends no information to us. It works offline and we have no servers that receive your data.'),
        ('Data stored on your device', 'Everything you write stays in the app’s private storage on your phone: your cards and their content, your drawers’ names and colors, your settings (language and sounds) and the photos you add. None of it leaves the phone unless you send or save a card as an image. It is deleted when you uninstall the app.'),
        ('Photos', 'When you add a photo to a card (for example in a tracker or a quote’s logo), you pick it yourself with the camera or the system picker, and the app keeps a copy in its own storage. The app does not browse or read the rest of your gallery. Camera permission is requested only when you tap to take a photo.'),
        ('Drawer codes', 'If you lock a drawer with a 4-digit code, the app does not store the code: it stores on your phone only a fingerprint of it in order to check it. The code prevents the drawer from being opened in the app, but it does not encrypt its contents. If you forget it, it cannot be recovered; the only way to remove it is to empty that drawer.'),
        ('Sending or saving a card', 'When you tap SEND, the app creates the card’s image (JPG) or PDF on your phone. If you choose to send it, the system share menu opens and you decide who gets it and how; whatever you send to another app is subject to that app’s privacy policy. If you choose to save it, on Android the image goes to your gallery (Pictures › My Kardek) and the PDF to Downloads › My Kardek; on iPhone the system menu opens, where you choose “Save Image” or “Save to Files”.'),
        ('Sounds and vibration', 'They are used only as effects when opening and closing drawers and cards. Sounds can be turned off in Settings.'),
        ('In-app purchases', 'The app is free. If you unlock the templates, the payment is processed by the store (Google Play or the App Store) with your store account, under the store’s own privacy policy. The app only asks the store whether the purchase exists, to unlock the templates; we never receive your payment or personal details.'),
        ('Children', 'The app is not directed at children under 13 and collects no data from anyone.'),
        ('Changes', 'If this policy changes, we will publish the new version on this same page with its date.'),
        ('Contact', f'For any privacy question, write to us at <a class="mail" href="mailto:{MAIL}">{MAIL}</a>'),
    ], '/kardek/privacidad/'),
}
for lang, (path, h1, meta, secs, alt_abs) in MK_PRIV.items():
    doc_page('kardek', lang, path, h1, meta, secs, alt_abs, 'game mk', 'mk-hero')

MK_SUP = {
    'es': ('kardek/soporte', 'Soporte', 'Escríbenos y te respondemos lo antes posible. Si es un error, cuéntanos el modelo de tu teléfono, la plantilla y qué estabas haciendo.', [
        ('¿Qué es gratis y qué se paga?', 'La app es gratis con cuatro plantillas: la hoja de cuaderno (líneas, cuadrícula, puntos o en blanco), No olvidar, ¿Qué estoy haciendo? y Mi semana. Las otras 44 se desbloquean juntas con un solo pago, para siempre: sin suscripción ni anuncios. La clave, la búsqueda y enviar en JPG o PDF son gratis.'),
        ('Cambié de teléfono o reinstalé la app y aparecen los candados.', 'Abre Ajustes y toca «RESTAURAR COMPRA», con la misma cuenta de Google Play (o Apple) con que compraste. Las plantillas vuelven sin pagar de nuevo. Tus fichas, en cambio, no se traspasan solas: quedan en el teléfono anterior.'),
        ('¿Cómo creo una ficha?', 'Abre un cajón y toca «+ FICHA». Desliza de lado para ver las plantillas completas, o toca una familia arriba para saltar a ella. Toca la plantilla del centro o «CREAR».'),
        ('¿Cómo le cambio el nombre a una ficha?', 'Con la ficha abierta, toca su nombre arriba (junto al lápiz) o la pestaña de la propia ficha. Ese es el nombre que asoma en el cajón.'),
        ('¿Cómo cambio el nombre o el color de un cajón?', 'En la pantalla del fichero toca «EDITAR CAJONES». Elige el cajón (01 a 04), escribe el nombre y toca un color de etiqueta.'),
        ('¿Cómo pongo o quito la clave de un cajón?', 'En «EDITAR CAJONES», elige el cajón y toca «PROTEGER CON CLAVE»: escribes 4 dígitos y los repites. Para quitarla, toca «QUITAR CLAVE» y escribe la clave actual. Para cambiarla, «CAMBIAR CLAVE».'),
        ('Olvidé la clave.', 'La clave no se puede recuperar, ni siquiera nosotros. En la pantalla de la clave toca «OLVIDÉ LA CLAVE»: la única forma de quitarla es vaciar ese cajón, y sus fichas se borran para siempre.'),
        ('¿Cómo envío o guardo una ficha?', 'Con la ficha abierta, toca «ENVIAR». Arriba elige el formato, «JPG · IMAGEN» o «PDF», y después «ENVIAR» para mandarla por WhatsApp, correo u otra app, o «GUARDAR EN EL TELÉFONO». En Android la imagen queda en la galería (Imágenes › My Kardek) y el PDF en Descargas › My Kardek; en iPhone elige «Guardar imagen» o «Guardar en Archivos» en el menú que aparece. La ficha sale de borde a borde, sin los botones de la app.'),
        ('¿Las cotizaciones calculan el total y el IVA?', 'No, a propósito: cada país y cada negocio calcula distinto. Escribes tú los valores, el neto, el impuesto y el total. Son un borrador rápido para mandar a un cliente, no una boleta ni una factura.'),
        ('¿Para qué son los presupuestos?', 'Para llevar las cuentas de una fiesta, un viaje o el mes: anotas cada gasto, marcas lo que ya pagaste y escribes el total gastado y lo que queda. Tampoco calculan solos; los montos los escribes tú.'),
        ('¿Cómo muevo, duplico o borro una ficha?', 'Con la ficha abierta, toca «⋯». Ahí puedes moverla a otro cajón, duplicarla o eliminarla. Si la eliminas, tienes unos segundos para tocar «DESHACER».'),
        ('El teclado tapa lo que escribo.', 'La ficha sube sola hasta lo que escribes, y también puedes moverla con el dedo. Al cerrar el teclado vuelve a su lugar.'),
        ('¿Cómo apago los sonidos o cambio el idioma?', 'En Ajustes (el engranaje en la pantalla del fichero): SONIDOS SÍ / NO e IDIOMA ESPAÑOL / ENGLISH. Las plantillas cambian de idioma; lo que tú escribiste, no.'),
        ('¿Dónde se guardan mis fichas?', 'Solo en tu teléfono. Si desinstalas la app o borras sus datos, se pierden y no tenemos copia. Para guardar una ficha importante fuera de la app, guárdala como imagen.'),
        ('¿Necesito internet?', 'No. My Kardek funciona entera sin conexión.'),
    ], '/kardek/support/', 'PREGUNTAS FRECUENTES'),
    'en': ('kardek/support', 'Support', "Write to us and we'll get back to you as soon as possible. If it's a bug, tell us your phone model, the template and what you were doing.", [
        ('What’s free and what’s paid?', 'The app is free with four templates: the notebook page (lines, grid, dots or blank), Note to self, What am I even doing? and My week. The other 44 unlock together with a single payment, forever: no subscription, no ads. Drawer codes, search and sending as JPG or PDF are free.'),
        ('I changed phones or reinstalled the app and the locks are back.', 'Open Settings and tap “RESTORE PURCHASE” with the same Google Play (or Apple) account you bought with. The templates come back without paying again. Your cards, however, don’t move on their own: they stay on the old phone.'),
        ('How do I create a card?', 'Open a drawer and tap “+ CARD”. Swipe sideways to see the templates in full, or tap a family at the top to jump to it. Tap the template in the middle or “CREATE”.'),
        ('How do I rename a card?', 'With the card open, tap its name at the top (next to the pencil) or the card’s own tab. That is the name that shows in the drawer.'),
        ('How do I change a drawer’s name or color?', 'On the card file screen tap “EDIT DRAWERS”. Choose the drawer (01 to 04), type the name and tap a label color.'),
        ('How do I lock or unlock a drawer?', 'In “EDIT DRAWERS”, choose the drawer and tap “LOCK WITH A CODE”: enter 4 digits and repeat them. To remove it, tap “REMOVE LOCK” and enter the current code. To change it, “CHANGE CODE”.'),
        ('I forgot the code.', 'The code cannot be recovered, not even by us. On the code screen tap “I FORGOT THE CODE”: the only way to remove it is to empty that drawer, and its cards are deleted for good.'),
        ('How do I send or save a card?', 'With the card open, tap “SEND”. At the top choose the format, “JPG · IMAGE” or “PDF”, then “SEND” to send it by WhatsApp, email or another app, or “SAVE TO PHONE”. On Android the image goes to your gallery (Pictures › My Kardek) and the PDF to Downloads › My Kardek; on iPhone choose “Save Image” or “Save to Files” in the menu that appears. The card comes out edge to edge, without the app’s buttons.'),
        ('Do quotes calculate the total and tax?', 'No, on purpose: every country and business calculates differently. You type the amounts, subtotal, tax and total yourself. They are a quick draft to send to a client, not an invoice.'),
        ('What are budgets for?', 'To keep track of a party, a trip or the month: you jot down each expense, tick what you have paid and write the total spent and what is left. They don’t calculate on their own either; you type the amounts.'),
        ('How do I move, duplicate or delete a card?', 'With the card open, tap “⋯”. There you can move it to another drawer, duplicate it or delete it. If you delete it, you have a few seconds to tap “UNDO”.'),
        ('The keyboard covers what I type.', 'The card scrolls up to what you are typing on its own, and you can also move it with your finger. When the keyboard closes it goes back into place.'),
        ('How do I turn off sounds or change the language?', 'In Settings (the gear on the card file screen): SOUNDS YES / NO and LANGUAGE ESPAÑOL / ENGLISH. Templates switch language; what you wrote does not.'),
        ('Where are my cards stored?', 'Only on your phone. If you uninstall the app or clear its data, they are lost and we keep no copy. To keep an important card outside the app, save it as an image.'),
        ('Do I need an internet connection?', 'No. My Kardek works fully offline.'),
    ], '/kardek/soporte/', 'FREQUENTLY ASKED QUESTIONS'),
}
for lang, (path, h1, lead, faq, alt_abs, faq_h) in MK_SUP.items():
    dl = ''.join(f'<dt>{q}</dt><dd>{a}</dd>' for q, a in faq)
    body = game_bar(lang, '{up}' + alt_abs.lstrip('/')) + f"""
<main id="main" class="wrap doc">
  <h1>{h1.upper()} · MY KARDEK</h1>
  <p>{lead}</p>
  <p><a class="mail" href="mailto:{MAIL}?subject=My%20Kardek">{MAIL}</a></p>
  <h2>{faq_h}</h2>
  <dl>{dl}</dl>
</main>
""" + game_footer(lang, 'kardek')
    page(path, lang, f'{h1} · My Kardek', f'{h1} · My Kardek · Estudio Treso', 'game mk', body, alt_abs, 2, og='mk-hero')

# Términos: app gratis con una compra única dentro de la app (todas las plantillas).
MK_TERMS_BUY = {
    'es': [('La app y la compra de plantillas', 'My Kardek es gratis y no tiene anuncios ni suscripción. Cuatro plantillas se usan sin pagar; las otras se desbloquean con una compra única dentro de la app. El precio se muestra en tu moneda antes de pagar. La compra queda asociada a tu cuenta de la tienda: puedes restaurarla en Ajustes, sin pagar de nuevo, usando la misma cuenta.'),
           ('Pagos y reembolsos', 'Los pagos los procesa Google Play o la App Store. Los reembolsos se rigen por las políticas de esa tienda; si tienes un problema con tu compra, escríbenos y te ayudamos.')],
    'en': [('The app and the template purchase', 'My Kardek is free and has no ads or subscription. Four templates can be used without paying; the other templates unlock with a one-time in-app purchase. The price is shown in your currency before you pay. The purchase is tied to your store account: you can restore it in Settings, without paying again, using the same account.'),
           ('Payments and refunds', 'Payments are processed by Google Play or the App Store. Refunds are governed by that store’s policies; if you have a problem with your purchase, write to us and we will help.')],
}
MK_TERMS_EXTRA = {
    'es': [('Tus fichas', 'Tus fichas y fotos se guardan solo en tu teléfono. No tenemos copia de ellas y no podemos recuperarlas si se pierden, por ejemplo al desinstalar la app o cambiar de teléfono.'),
           ('Clave de los cajones', 'La clave de 4 dígitos impide abrir un cajón desde la app, pero no cifra su contenido. Si la olvidas no se puede recuperar: la única forma de quitarla es vaciar ese cajón, con lo que sus fichas se borran.'),
           ('Cotizaciones y presupuestos', 'Las plantillas de cotización y de presupuesto son para llenar a mano: no calculan totales ni impuestos y no son documentos tributarios (boleta, factura ni equivalentes). Eres responsable de los valores, impuestos y condiciones que escribes y de lo que envías a tus clientes.'),
           ('Tu contenido', 'Lo que escribes y las fotos que agregas son tuyos. Eres responsable de tener derecho a usar las fotos y logos que pongas en tus fichas.')],
    'en': [('Your cards', 'Your cards and photos are stored only on your phone. We keep no copy of them and cannot recover them if they are lost, for example when uninstalling the app or changing phones.'),
           ('Drawer codes', 'The 4-digit code prevents a drawer from being opened in the app, but it does not encrypt its contents. If you forget it, it cannot be recovered: the only way to remove it is to empty that drawer, which deletes its cards.'),
           ('Quotes and budgets', 'Quote and budget templates are filled in by hand: they do not calculate totals or taxes and they are not tax documents (invoices, receipts or equivalents). You are responsible for the amounts, taxes and conditions you write and for what you send to your clients.'),
           ('Your content', 'What you write and the photos you add are yours. You are responsible for having the right to use the photos and logos you put on your cards.')],
}
for lang in ('es', 'en'):
    secs = terms(lang, 'My Kardek', 'una app de notas' if lang == 'es' else 'a note-taking app', '', MK_TERMS_EXTRA[lang])
    secs[2:4] = MK_TERMS_BUY[lang]
    doc_page('kardek', lang, 'kardek/terminos' if lang == 'es' else 'kardek/terms', 'Términos del servicio' if lang == 'es' else 'Terms of Service',
             ('Última actualización: ' if lang == 'es' else 'Last updated: ') + UPDATED_MK[lang], secs,
             '/kardek/terms/' if lang == 'es' else '/kardek/terminos/', 'game mk', 'mk-hero')
