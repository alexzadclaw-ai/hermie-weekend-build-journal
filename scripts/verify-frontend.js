const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const file = path.resolve(__dirname, '..', 'index.html');
  const url = 'file://' + file;
  const messages = [];
  const failures = [];
  const browser = await chromium.launch({ executablePath: '/snap/bin/chromium', headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 1200 } });
  page.on('console', msg => messages.push({ type: msg.type(), text: msg.text() }));
  page.on('pageerror', err => failures.push({ type: 'pageerror', text: err.message }));
  page.on('requestfailed', req => failures.push({ type: 'requestfailed', url: req.url(), text: req.failure()?.errorText }));
  await page.goto(url, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(500);
  const result = await page.evaluate(() => ({
    title: document.title,
    cards: document.querySelectorAll('.post-card').length,
    hasHero: document.body.innerText.includes('From a first hello to a live local brand'),
    hasBusiness: document.body.innerText.includes('Clean now. Monetizable later.'),
    postDataCount: JSON.parse(document.getElementById('postData').textContent).length
  }));
  await page.click('a[href^="#post-"]');
  await page.waitForTimeout(300);
  const modal = await page.evaluate(() => ({
    open: document.querySelector('#reader').classList.contains('open'),
    articleChars: document.querySelector('#article').innerText.length,
    title: document.querySelector('#readerTitle').innerText
  }));
  await browser.close();
  console.log(JSON.stringify({ result, modal, console: messages, failures }, null, 2));
  if (failures.length || messages.some(m => ['error'].includes(m.type)) || result.cards !== 7 || result.postDataCount !== 7 || !modal.open || modal.articleChars < 1000) {
    process.exit(1);
  }
})();
