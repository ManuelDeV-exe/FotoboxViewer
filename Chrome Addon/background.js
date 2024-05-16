let intervalId = null;

chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.local.set({ refreshInterval: 1, isEnabled: false }, handleAutoRefresh);
});

chrome.storage.onChanged.addListener((changes, area) => {
  if (area === 'local' && (changes.refreshInterval || changes.isEnabled)) {
    handleAutoRefresh();
  }
});

function handleAutoRefresh() {
  chrome.storage.local.get(['refreshInterval', 'isEnabled'], (result) => {
    const { refreshInterval = 1, isEnabled = false } = result;

    if (intervalId) {
      clearInterval(intervalId);
      intervalId = null;
    }

    if (isEnabled) {
      chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        if (tabs.length > 0) {
          const tabId = tabs[0].id;
          intervalId = setInterval(() => {
            chrome.tabs.reload(tabId);
          }, refreshInterval * 60000);
        }
      });
      chrome.action.setBadgeText({ text: 'ON' });
    } else {
      chrome.action.setBadgeText({ text: '' });
    }
  });
}
