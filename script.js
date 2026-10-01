'use strict';
document.documentElement.classList.replace('no-js', 'js');
const menuButton = document.querySelector('[data-menu]');
const navigation = document.querySelector('[data-nav]');
function closeMenu(returnFocus = false) {
  const wasOpen = menuButton?.getAttribute('aria-expanded') === 'true';
  menuButton?.setAttribute('aria-expanded', 'false');
  navigation?.classList.remove('is-open');
  document.body.classList.remove('menu-open');
  if (returnFocus && wasOpen) menuButton?.focus();
}
menuButton?.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.setAttribute('aria-expanded', String(open));
  navigation.classList.toggle('is-open', open);
  document.body.classList.toggle('menu-open', open);
});
navigation?.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(true); });
document.addEventListener('click', event => { if (!event.target.closest('.site-header')) closeMenu(); });
document.addEventListener('focusin', event => { if (!event.target.closest('.site-header')) closeMenu(); });
window.matchMedia('(min-width: 801px)').addEventListener('change', () => closeMenu());

// Static email composer. No data is sent or stored by the website.
const form = document.querySelector('[data-inquiry]');
if (form) {
  form.hidden = false;
  const status = document.querySelector('[data-form-status]');
  function draft() {
    const data = new FormData(form);
    const value = key => String(data.get(key) || '').trim();
    return {
      subject: 'Business inquiry: ' + value('interest') + ' — ' + value('company'),
      body: 'Hello Nalston,\n\n' + value('message') + '\n\nName: ' + value('name') + '\nCompany: ' + value('company') + '\nEmail: ' + value('email') + '\nInterest: ' + value('interest') + '\nMarket: ' + value('market') + '\n'
    };
  }
  form.addEventListener('submit', event => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const { subject, body } = draft();
    window.location.href = 'mailto:nicolas@nalstongroup.com?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    status.textContent = 'Your email app has been requested. Review and send the draft there. Nothing has been sent by this website. If no app opens, use Copy inquiry and email us directly.';
  });
  document.querySelector('[data-copy-inquiry]').addEventListener('click', async () => {
    if (!form.reportValidity()) return;
    const { subject, body } = draft();
    try {
      await navigator.clipboard.writeText('To: nicolas@nalstongroup.com\nSubject: ' + subject + '\n\n' + body);
      status.textContent = 'Inquiry copied. Paste it into an email to nicolas@nalstongroup.com and send it from your email account.';
    } catch {
      status.textContent = 'Clipboard access is unavailable. Please copy your message manually and email nicolas@nalstongroup.com.';
    }
  });
}
