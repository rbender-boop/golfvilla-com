/* GolfVilla.com — main.js v1 */

// ── NAV SCROLL ──────────────────────────────────────────────────
const nav = document.getElementById('main-nav') || document.querySelector('.site-nav');
if (nav) {
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 60);
  });
}

// ── MOBILE MENU ──────────────────────────────────────────────────
const hamburger = document.querySelector('.nav-hamburger');
const mobileMenu = document.querySelector('.mobile-menu');
const mobileClose = document.querySelector('.mobile-close');
if (hamburger && mobileMenu) {
  hamburger.addEventListener('click', () => mobileMenu.classList.add('open'));
}
if (mobileClose && mobileMenu) {
  mobileClose.addEventListener('click', () => mobileMenu.classList.remove('open'));
}

// ── FADE-UP ON SCROLL ────────────────────────────────────────────
const fadeEls = document.querySelectorAll('.fade-up');
if (fadeEls.length) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); observer.unobserve(e.target); } });
  }, { threshold: 0.1 });
  fadeEls.forEach(el => observer.observe(el));
}


// ── FAQ ACCORDION ────────────────────────────────────────────────
document.querySelectorAll('.faq-q').forEach(btn => {
  btn.addEventListener('click', () => {
    const expanded = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', !expanded);
    const answer = btn.nextElementSibling;
    answer.classList.toggle('open', !expanded);
  });
});
