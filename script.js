(() => {
  'use strict';
  const root = document.documentElement;
  const themeButton = document.querySelector('.theme-toggle');
  const colorPreference = window.matchMedia('(prefers-color-scheme: dark)');
  let savedTheme = null;
  try { savedTheme = localStorage.getItem('navid-theme'); } catch (_) { /* Storage is optional. */ }
  const applyTheme = (theme) => {
    root.dataset.theme = theme;
    themeButton.setAttribute('aria-pressed', String(theme === 'dark'));
    themeButton.setAttribute('aria-label', `Switch to ${theme === 'dark' ? 'light' : 'dark'} theme`);
    document.querySelector('meta[name="theme-color"]').content = theme === 'dark' ? '#1f2220' : '#ffffff';
  };
  applyTheme(savedTheme === 'dark' || savedTheme === 'light' ? savedTheme : (colorPreference.matches ? 'dark' : 'light'));
  themeButton.addEventListener('click', () => {
    savedTheme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    applyTheme(savedTheme);
    try { localStorage.setItem('navid-theme', savedTheme); } catch (_) { /* Theme works without storage. */ }
  });
  colorPreference.addEventListener('change', (event) => { if (!savedTheme) applyTheme(event.matches ? 'dark' : 'light'); });
  document.querySelector('#copyright-year').textContent = new Date().getFullYear();

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  document.querySelectorAll('[data-carousel]').forEach((section) => {
    const track = section.querySelector('.academic-track');
    const previous = section.querySelector('[data-direction="previous"]');
    const next = section.querySelector('[data-direction="next"]');
    const updateControls = () => {
      previous.disabled = track.scrollLeft < 2;
      next.disabled = track.scrollLeft >= track.scrollWidth - track.clientWidth - 2;
    };
    const move = (direction) => {
      const cards = [...track.children];
      const trackLeft = track.getBoundingClientRect().left;
      const positions = cards.map((card) => card.getBoundingClientRect().left - trackLeft + track.scrollLeft);
      const target = direction > 0
        ? positions.find((position) => position > track.scrollLeft + 5)
        : positions.reverse().find((position) => position < track.scrollLeft - 5);
      if (target !== undefined) {
        track.scrollTo({left: target, behavior: reduceMotion.matches ? 'instant' : 'smooth'});
      }
    };
    previous.addEventListener('click', () => move(-1));
    next.addEventListener('click', () => move(1));
    track.addEventListener('keydown', (event) => {
      if (event.target !== track) return;
      if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') {
        event.preventDefault();
        move(event.key === 'ArrowRight' ? 1 : -1);
      }
      if (event.key === 'Home' || event.key === 'End') {
        event.preventDefault();
        track.scrollTo({left: event.key === 'Home' ? 0 : track.scrollWidth, behavior: reduceMotion.matches ? 'instant' : 'smooth'});
      }
    });
    track.addEventListener('scroll', updateControls, {passive: true});
    if ('ResizeObserver' in window) new ResizeObserver(updateControls).observe(track);
    else window.addEventListener('resize', updateControls);
    updateControls();
  });
})();
