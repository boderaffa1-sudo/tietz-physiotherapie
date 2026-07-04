// Map (OpenFreeMap, no API key needed)
(function () {
  const el = document.getElementById('map');
  if (!el || !window.maplibregl) return;
  const map = new maplibregl.Map({
    container: 'map',
    style: 'https://tiles.openfreemap.org/styles/positron',
    center: [13.293, 52.499], // Lützenstraße 13, 10711 Berlin (Halensee)
    zoom: 15,
    interactive: true,
  });
  map.addControl(new maplibregl.NavigationControl(), 'top-right');
  map.on('load', () => {
    new maplibregl.Marker({ color: '#b3562f' })
      .setLngLat([13.293, 52.499])
      .setPopup(new maplibregl.Popup().setHTML('<strong>Praxis Tietz</strong><br>Lützenstraße 13, 10711 Berlin'))
      .addTo(map);
  });
})();

// File upload filename display
(function () {
  const input = document.getElementById('rxUpload');
  const label = document.getElementById('rxFileName');
  if (!input || !label) return;
  input.addEventListener('change', () => {
    if (input.files && input.files[0]) {
      label.textContent = 'Ausgewählt: ' + input.files[0].name;
    }
  });
})();

// Contact form (demo — no backend wired yet)
(function () {
  const form = document.getElementById('contactForm');
  const note = document.getElementById('formNote');
  if (!form) return;
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    note.textContent = 'Danke für Ihre Nachricht! Diese Demo-Seite versendet noch keine echten Anfragen — bitte nutzen Sie bis zum Livegang Telefon oder E-Mail.';
    note.style.color = 'var(--color-primary)';
    note.style.fontWeight = '600';
  });
})();
