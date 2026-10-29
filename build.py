"""Genera las páginas de estudio.treso.cl (español e inglés). Uso: python3 build.py"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
MAIL = 'contacto@treso.cl'
SITE = 'https://estudio.treso.cl'
UPDATED = {'es': '28 de octubre de 2026', 'en': 'October 28, 2026'}

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@600;700&family=Fira+Sans:wght@400;500;800&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">')


def page(path, lang, title, desc, body_class, body, alt_href, depth):
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
<meta property="og:image" content="{SITE}/assets/d40-hero-{lang}.jpg">
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


def game_footer(lang):
    if lang == 'es':
        links = [('{up}', 'Todos los juegos y apps'), ('{up}depth40/', 'Depth 40'), ('{up}depth40/soporte/', 'Soporte'), ('{up}depth40/privacidad/', 'Privacidad')]
    else:
        links = [('{up}en/', 'All games and apps'), ('{up}depth40/en/', 'Depth 40'), ('{up}depth40/support/', 'Support'), ('{up}depth40/privacy/', 'Privacy')]
    nav = ''.join(f'<a href="{h}">{t}</a>' for h, t in links)
    return f'''<div class="wrap"><footer><span>© 2026 TRESO SPA · Santiago, Chile</span><nav>{nav}</nav></footer></div>'''


# ---------------------------------------------------------------- inicio del estudio
# Catálogo: cada juego o app tiene su carpeta (/slug/, /slug/en/, /slug/soporte/, /slug/privacidad/ ...).
# Para agregar uno nuevo: sumarlo aquí y crear sus páginas abajo, igual que Depth 40.
CATALOG = [
    dict(slug='depth40', kind={'es': 'JUEGO', 'en': 'GAME'}, name='DEPTH <em>40</em>', label='Depth 40', pic='d40-hero',
         p={'es': 'Sigilo en submarino. Ocho misiones bajo el mar y el hielo, sin ver nunca el exterior: solo sonar, periscopio y silencio.',
            'en': 'Submarine stealth. Eight missions under the sea and the ice, never seeing the outside: only sonar, periscope and silence.'},
         status={'es': 'PRÓXIMAMENTE · ANDROID Y IPHONE', 'en': 'COMING SOON · ANDROID AND IPHONE'}),
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
  <a class="game-card" href="{href}">
    <div class="pic" style="background-image:url('{{up}}assets/{c['pic']}-{lang}.jpg')" role="img" aria-label="{c['label']}"></div>
    <div class="txt"><span class="k">{c['kind'][lang]} · {c['status'][lang]}</span><h2>{c['name']}</h2><p>{c['p'][lang]}</p><span class="go">{t['go']}</span></div>
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
        pills=['8 MISIONES', 'ESPAÑOL · ENGLISH', 'SIN ANUNCIOS', 'SIN COMPRAS', 'SIN INTERNET'],
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
        pills=['8 MISSIONS', 'ENGLISH · ESPAÑOL', 'NO ADS', 'NO PURCHASES', 'NO INTERNET NEEDED'],
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
    pills = f'<span class="pill soon">{t["soon"]}</span>' + ''.join(f'<span class="pill">{p}</span>' for p in t['pills'])
    body = game_bar(lang, alt) + f'''
<main id="main" class="wrap">
  <div class="hero" style="background-image:url('{{up}}assets/d40-hero-{lang}.jpg')" role="img" aria-label="Depth 40"></div>
  <h1>DEPTH <em>40</em></h1>
  <p class="tag">{t['tag']}</p>
  {''.join(f'<p class="intro">{p}</p>' for p in t['intro'])}
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
        ('Datos que recopilamos', 'Ninguno. Depth 40 no pide registro, no usa cuentas, no muestra publicidad, no tiene compras dentro de la app y no envía información a internet.'),
        ('Datos guardados en tu dispositivo', 'El juego guarda en tu propio teléfono el idioma elegido, tus ajustes (música, efectos, vibración, color de pantalla) y las misiones cumplidas. Esa información no sale del dispositivo, no la recibimos y se borra al desinstalar el juego o al usar «Reiniciar progreso» en Ajustes.'),
        ('Permisos', 'Depth 40 no usa cámara, micrófono, ubicación, contactos ni otros datos personales. La vibración se usa solo como efecto del juego y puede apagarse en Ajustes.'),
        ('Terceros', 'El juego no incluye servicios de análisis, publicidad ni otros servicios de terceros que recopilen datos.'),
        ('Niños', 'El juego no está dirigido a menores de 13 años y no recopila datos de nadie.'),
        ('Cambios', 'Si esta política cambia, publicaremos la nueva versión en esta misma página con su fecha.'),
        ('Contacto', f'Para cualquier consulta sobre privacidad escríbenos a <a class="mail" href="mailto:{MAIL}">{MAIL}</a>'),
    ], '{up}depth40/privacy/', '/depth40/privacy/'),
    'en': ('depth40/privacy', 'Privacy Policy', 'Depth 40', f'Last updated: {UPDATED["en"]}', [
        ('', 'Depth 40 is a game developed by Estudio Treso, a brand of TRESO SPA (Santiago, Chile).'),
        ('Data we collect', 'None. Depth 40 requires no sign-up, has no accounts, shows no ads, has no in-app purchases and sends no information over the internet.'),
        ('Data stored on your device', 'The game stores on your own phone the language you chose, your settings (music, effects, vibration, screen color) and the missions you completed. This information never leaves the device, we never receive it, and it is deleted when you uninstall the game or use “Reset progress” in Settings.'),
        ('Permissions', 'Depth 40 does not use the camera, microphone, location, contacts or any other personal data. Vibration is used only as a game effect and can be turned off in Settings.'),
        ('Third parties', 'The game includes no analytics, advertising or other third-party services that collect data.'),
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
        ('¿Necesito internet?', 'No. Depth 40 funciona completo sin conexión.'),
        ('Me detectan siempre. ¿Algún consejo?', 'Ve más lento, baja más hondo y usa el modo SILENCIO cuando te busquen. Bajo un témpano o bajo la capa de 100 m el sonar enemigo casi no te ve.'),
    ], '{up}depth40/support/', '/depth40/support/', 'PREGUNTAS FRECUENTES'),
    'en': ('depth40/support', 'Support', "Write to us and we'll get back to you as soon as possible. If it's a bug, tell us your phone model, the mission and what you were doing.", [
        ('How do I change the language?', 'On the main menu, tap SETTINGS and choose ENGLISH or ESPAÑOL.'),
        ("I can't hear anything.", "Check that your phone isn't on silent and that music and effects are on in SETTINGS. Sound starts with your first tap on the screen."),
        ('How do I see the tutorial again?', 'In SETTINGS, tap “View tutorial”. Each mission briefing also has a VIEW TUTORIAL button.'),
        ('I lost my progress.', 'Progress is saved only on your phone. If you uninstall the game or clear its data, it is lost. “Reset progress” in SETTINGS also erases it.'),
        ('Do I need an internet connection?', 'No. Depth 40 works fully offline.'),
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
