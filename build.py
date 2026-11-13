"""Genera las páginas de estudio.treso.cl (español e inglés). Uso: python3 build.py"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
MAIL = 'contacto@treso.cl'
SITE = 'https://estudio.treso.cl'
UPDATED = {'es': '3 de noviembre de 2026', 'en': 'November 3, 2026'}
UPDATED_WD = {'es': '5 de noviembre de 2026', 'en': 'November 5, 2026'}

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@600;700&family=Fira+Sans:wght@400;500;800&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">')


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
  <a class="lang" href="{alt}" hreflang="{'en' if lang == 'es' else 'es'}">{'ENGLISH' if lang == 'es' else 'ESPAÑOL'}</a>
</header></div>'''


def game_bar(lang, alt):
    home = '{up}' + ('' if lang == 'es' else 'en/')
    return f'''<div class="wrap"><header class="bar">
  <a class="mini" href="{home}"><img src="{{up}}assets/logo.svg" alt="">ESTUDIO TRESO</a>
  <a class="lang" href="{alt}" hreflang="{'en' if lang == 'es' else 'es'}">{'ENGLISH' if lang == 'es' else 'ESPAÑOL'}</a>
</header></div>'''


PRODUCT_NAME = {'depth40': 'Depth 40', 'widgetdesign': 'Widget Design'}


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
    'depth40': {'android': None, 'ios': None},
    'widgetdesign': {'android': None, 'ios': None},   # Google Play: https://play.google.com/store/apps/details?id=cl.treso.widgetdesign
}
PLAT = {'android': ('Google Play', 'Android'), 'ios': ('App Store', 'iPhone')}


def platforms_line(slug, lang):
    st = STORES[slug]
    names = [PLAT[k][1] for k in ('android', 'ios') if k in st]
    both = (' y ' if lang == 'es' else ' and ').join(names)
    live = all(st[k] for k in st)
    if live:
        return ('DISPONIBLE · ' if lang == 'es' else 'AVAILABLE · ') + both.upper()
    return ('PRÓXIMAMENTE · ' if lang == 'es' else 'COMING SOON · ') + both.upper()


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
<div class="wrap"><footer><span>© 2026 TRESO SPA · Santiago, Chile</span><span>{t['contact']}: <a href="mailto:{MAIL}">{MAIL}</a></span></footer></div>'''
    page(path, lang, 'Estudio Treso', t['lead'], 'studio', body, '/en/' if lang == 'es' else '/', 0 if lang == 'es' else 1)

# ---------------------------------------------------------------- Depth 40
D40 = {
    'es': dict(
        tag='SIGILO EN SUBMARINO', soon='PRÓXIMAMENTE EN GOOGLE PLAY Y APP STORE',
        intro=['Eres el capitán. Desde la consola de mando decides el rumbo, la velocidad y la profundidad. Cada ruido que haces puede delatarte.',
               'Depth 40 es un juego de sigilo en primera persona dentro de un submarino. No ves el mar: lo escuchas. El sonar, el periscopio y tu instinto son lo único que tienes.'],
        pills=['8 MISIONES', 'ESPAÑOL · ENGLISH', '2 MISIONES GRATIS', 'PAGO ÚNICO', 'SIN ANUNCIOS', 'SIN INTERNET'],
        shots_h='CAPTURAS', feat_h='LA CONSOLA',
        feats=[('Sonar pasivo y activo', 'Escucha sin ser oído. El ping da distancias exactas, pero te delata.'),
               ('Periscopio', 'La única vista real del exterior, y solo a cota 20 m.'),
               ('Modo silencio', 'Apaga todo lo que hace ruido y espera a que el enemigo se rinda.'),
               ('Armas', 'Torpedos rectos y filoguiados, misil, señuelos y ametralladora.')],
        mis_h='PRIMERA TEMPORADA', mis=['Aguas ajenas', 'Blanco quieto', 'Blanco en movimiento', 'Cazador', 'Rescate bajo el hielo', 'Pesqueros', 'Señuelo', 'Orden sellada'],
        alt='Capturas de Depth 40', shots=['inicio', 'misiones', 'brief', 'consola', 'hielo'],
        shot_alt=['Menú principal', 'Archivador de misiones', 'Instrucciones de la misión 4', 'Consola de mando', 'Misión 8 bajo el hielo'],
        desc='Depth 40: sigilo en submarino. Ocho misiones para Android y iPhone. Un juego de Estudio Treso.'),
    'en': dict(
        tag='SUBMARINE STEALTH', soon='COMING SOON TO GOOGLE PLAY AND THE APP STORE',
        intro=['You are the captain. From the command console you set the heading, the speed and the depth. Every sound you make can give you away.',
               "Depth 40 is a first-person stealth game set inside a submarine. You don't see the sea: you hear it. Sonar, periscope and instinct are all you have."],
        pills=['8 MISSIONS', 'ENGLISH · ESPAÑOL', '2 FREE MISSIONS', 'ONE-TIME PURCHASE', 'NO ADS', 'NO INTERNET NEEDED'],
        shots_h='SCREENSHOTS', feat_h='THE CONSOLE',
        feats=[('Passive and active sonar', 'Listen without being heard. A ping gives exact distances, but gives you away.'),
               ('Periscope', 'The only real view outside, and only at 20 m.'),
               ('Silent running', 'Shut down everything that makes noise and wait for the enemy to give up.'),
               ('Weapons', 'Straight and wire-guided torpedoes, a missile, decoys and a machine gun.')],
        mis_h='SEASON ONE', mis=['Foreign waters', 'Still target', 'Moving target', 'Hunter', 'Rescue under the ice', 'Fishing boats', 'Decoy', 'Sealed order'],
        alt='Depth 40 screenshots', shots=['inicio', 'misiones', 'brief', 'consola', 'hielo'],
        shot_alt=['Main menu', 'Mission files', 'Mission 4 briefing', 'Command console', 'Mission 8 under the ice'],
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
