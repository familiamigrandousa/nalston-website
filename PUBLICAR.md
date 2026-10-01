# Publicar NALSTON

## 1. Subir la nueva versión a GitHub Pages

Abre PowerShell en esta carpeta y ejecuta:

```powershell
cd "C:\Users\nicol\OneDrive\Escritorio\nalston-premium-v2"
git add .
git commit -m "Launch redesigned Nalston corporate website"
git push origin main
```

Esto publica los cambios si Pages ya usa la rama main. Los PDF privados no se copiaron al repositorio; las pruebas locales están excluidas mediante .gitignore.

En [el repositorio](https://github.com/familiamigrandousa/nalston-website), abre **Settings → Pages**. Para este sitio estático, la configuración es **Deploy from a branch → main → / (root)**. Guarda si necesitas corregirla. Si ya existe una configuración funcional de Pages, consérvala.

En **Actions**, espera a que termine correctamente el despliegue de Pages. Después abre:

https://familiamigrandousa.github.io/nalston-website/

Recarga con Ctrl+F5 y comprueba portada, Contact, teléfono y fotos. Si Git rechaza el push por cambios remotos, no uses --force: revisa y sincroniza los cambios antes de reintentar.

Fuente: [configuración oficial de GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## 2. Conectar nalstongroup.com

Primero publica y revisa la versión anterior. Después:

1. En **Settings → Pages → Custom domain**, introduce **nalstongroup.com** y guarda.
2. Abre el administrador DNS del dominio y configura estos registros web:

| Tipo | Nombre / Host | Valor / Destino |
| --- | --- | --- |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | familiamigrandousa.github.io |

El CNAME no lleva https ni /nalston-website. Revisa los registros web anteriores de @ y www para evitar destinos incompatibles; no borres registros de correo. Mantén MX y TXT de SPF, DKIM y DMARC.

3. Espera la comprobación DNS de GitHub; la propagación puede tardar hasta 24 horas. Activa **Enforce HTTPS** cuando esté disponible.
4. Comprueba https://nalstongroup.com y https://www.nalstongroup.com.

Valores verificados el 1 de octubre de 2026 en la [documentación oficial de dominios de GitHub Pages](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site). Si haces la configuración más adelante, comprueba de nuevo esa página.

## 3. Actualizar SEO al dominio definitivo

Al guardar el dominio, GitHub puede crear un commit con CNAME. Sincroniza primero:

```powershell
git pull --ff-only origin main
& "C:\Users\nicol\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" tools/set_site_url.py https://nalstongroup.com/
git add .
git commit -m "Use nalstongroup.com as canonical domain"
git push origin main
```

La ruta de Python indicada corresponde al runtime disponible en este equipo. Si tienes Python instalado por separado, puedes usar python en lugar de esa ruta.

El script actualiza canonical, Open Graph, datos estructurados, robots, sitemap y la base de la página 404. No cambia el correo.

## Datos públicos actuales

- Marca: NALSTON.
- Nombre legal: Nalston Strategic Group LLC.
- Email: nicolas@nalstongroup.com.
- Teléfono: +1 (727) 621-2884, con enlaces para llamar.
- Dirección: pendiente de confirmar que es válida para recibir correspondencia comercial pública; no se presenta como oficina.
- El EIN y los documentos corporativos no se publican.

El formulario prepara un correo; la persona debe enviarlo desde su aplicación de email.
