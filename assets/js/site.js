// Mark Anthony Maina — portfolio interactions. No dependencies.
(function () {
  var doc = document.documentElement;
  var header = document.querySelector('.header');

  // Header: solid background once the page scrolls.
  function onScroll() {
    if (!header) return;
    header.classList.toggle('scrolled', window.scrollY > 24);
  }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Mobile menu.
  var menuBtn = document.querySelector('.menu-btn');
  if (menuBtn) {
    menuBtn.addEventListener('click', function () {
      var open = doc.classList.toggle('menu-open');
      menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.querySelectorAll('.mobile-nav a').forEach(function (a) {
      a.addEventListener('click', function () { doc.classList.remove('menu-open'); });
    });
  }

  // Services dropdown: keyboard / touch support (hover handles desktop mouse).
  document.querySelectorAll('.nav-drop > button').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var wrap = btn.parentElement;
      var open = wrap.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function () {
    document.querySelectorAll('.nav-drop.open').forEach(function (d) { d.classList.remove('open'); });
  });

  // Reveal on scroll + chart draw.
  var targets = document.querySelectorAll('.reveal, .anim');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.classList.add('in');
          countUp(en.target);
          io.unobserve(en.target);
        }
      });
    }, { threshold: 0.18, rootMargin: '0px 0px -40px 0px' });
    targets.forEach(function (t) { io.observe(t); });
  } else {
    targets.forEach(function (t) { t.classList.add('in'); });
  }

  // Count-up numbers: <b data-count="47" data-prefix="+" data-suffix="%">
  function countUp(scope) {
    var els = scope.matches && scope.matches('[data-count]') ? [scope] : scope.querySelectorAll('[data-count]');
    els.forEach(function (el) {
      if (el.dataset.done) return;
      el.dataset.done = '1';
      var end = parseFloat(el.dataset.count);
      var dec = (el.dataset.count.split('.')[1] || '').length;
      var pre = el.dataset.prefix || '', suf = el.dataset.suffix || '';
      var start = null, dur = 1400;
      if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) { el.textContent = pre + end.toFixed(dec) + suf; return; }
      function step(ts) {
        if (!start) start = ts;
        var p = Math.min((ts - start) / dur, 1);
        var e = 1 - Math.pow(1 - p, 3);
        el.textContent = pre + (end * e).toLocaleString('en-US', { minimumFractionDigits: dec, maximumFractionDigits: dec }) + suf;
        if (p < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    });
  }

  // Contact form: open the visitor's mail client with everything filled in,
  // so no enquiry is silently lost to a broken form backend.
  document.querySelectorAll('form[data-mailto]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var f = form.elements;
      var name = (f.name.value || '').trim();
      var email = (f.email.value || '').trim();
      var topic = f.topic ? f.topic.value : '';
      var msg = (f.message.value || '').trim();
      var subject = (topic ? topic + ' — ' : '') + 'Enquiry from ' + (name || 'your website');
      var body = msg + '\n\n--\n' + name + (email ? '\n' + email : '') + (f.company && f.company.value ? '\n' + f.company.value : '');
      window.location.href = 'mailto:' + form.dataset.mailto + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    });
  });

  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
