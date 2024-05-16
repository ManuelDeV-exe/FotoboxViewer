document.getElementById('save').addEventListener('click', () => {
  const interval = parseInt(document.getElementById('interval').value);
  chrome.storage.local.set({ refreshInterval: interval }, () => {
    alert('Interval set to ' + interval + ' minutes.');
  });
});

document.getElementById('enable').addEventListener('change', (event) => {
  chrome.storage.local.set({ isEnabled: event.target.checked });
});

document.addEventListener('DOMContentLoaded', () => {
  chrome.storage.local.get(['refreshInterval', 'isEnabled'], (result) => {
    document.getElementById('interval').value = result.refreshInterval || 1;
    document.getElementById('enable').checked = result.isEnabled || false;
  });
});
