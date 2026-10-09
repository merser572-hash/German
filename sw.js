const CACHE_NAME = 'wunderdeutsch-v39';
const ASSETS_TO_CACHE = [
    './',
    './index.html',
    './style.css',
    './grammar-rules.js',
    './app.js',
    './manifest.json',
    './words.json',
    './sentences.json',
    './sortable.min.js'
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
        .then(cache => cache.addAll(ASSETS_TO_CACHE))
        .then(() => self.skipWaiting())
    );
});

self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(keys => {
            return Promise.all(
                keys.map(key => {
                    if (key !== CACHE_NAME) return caches.delete(key);
                })
            );
        }).then(() => self.clients.claim())
    );
});

// Stale-While-Revalidate Strategy (Allows offline, but forces updates)
self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request).then(cachedResponse => {
            const fetchPromise = fetch(event.request).then(networkResponse => {
                caches.open(CACHE_NAME).then(cache => {
                    cache.put(event.request, networkResponse.clone());
                });
                return networkResponse;
            }).catch(() => {
                // Ignore network errors if offline
            });
            return cachedResponse || fetchPromise;
        })
    );
});
