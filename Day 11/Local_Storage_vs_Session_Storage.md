# Local Storage vs Session Storage

## Introduction

Local Storage and Session Storage are web storage mechanisms provided by browsers that allow websites to store data on the client side. Both are part of the Web Storage API and store data as key-value pairs.

## What is Local Storage?

Local Storage stores data permanently in the user's browser until it is manually removed by the user or cleared by the application.

### Features of Local Storage

- Data persists even after the browser is closed.
- Storage capacity is typically around 5–10 MB.
- Data is accessible from all tabs and windows of the same origin.
- Stores data as key-value pairs.

### Common Uses

- User preferences
- Theme settings (dark/light mode)
- Remembering user choices
- Offline web applications

## What is Session Storage?

Session Storage stores data only for the duration of a browser session.

### Features of Session Storage

- Data is cleared when the tab or browser window is closed.
- Data is available only within the current tab.
- Storage capacity is typically around 5 MB.
- Stores data as key-value pairs.

### Common Uses

- Temporary form data
- Multi-step forms
- Session-specific information
- Temporary user activity tracking

## Key Differences

| Feature | Local Storage | Session Storage |
|----------|---------------|----------------|
| Lifetime | Until manually deleted | Until tab/window is closed |
| Storage Limit | About 5–10 MB | About 5 MB |
| Scope | Shared across tabs of same origin | Available only in current tab |
| Persistence | Permanent | Temporary |
| Browser Restart | Data remains | Data is removed |

## Local Storage Example

```javascript
// Store data
localStorage.setItem("username", "Tanisha");

// Retrieve data
let user = localStorage.getItem("username");

// Remove data
localStorage.removeItem("username");

// Clear all data
localStorage.clear();
```

## Session Storage Example

```javascript
// Store data
sessionStorage.setItem("username", "Tanisha");

// Retrieve data
let user = sessionStorage.getItem("username");

// Remove data
sessionStorage.removeItem("username");

// Clear all data
sessionStorage.clear();
```

## Advantages of Local Storage

- Data persists for a long time.
- Easy to use.
- Useful for saving user preferences.
- Reduces repeated server requests.

## Advantages of Session Storage

- Ideal for temporary data.
- Automatically clears after the session ends.
- Better for sensitive short-term information.

## Limitations

- Stores only strings.
- Not suitable for large amounts of data.
- Data can be accessed through browser developer tools.
- Should not be used to store sensitive information like passwords.

## When to Use Local Storage

- Theme preferences
- Language settings
- Remembering user choices
- Offline data caching

## When to Use Session Storage

- Login session information
- Temporary form data
- One-time user actions
- Data needed only during the current browsing session

## Conclusion

Local Storage and Session Storage are useful browser-based storage options. Local Storage is best for long-term data that should remain available across browser sessions, while Session Storage is ideal for temporary data that should be removed when the user closes the tab or browser window.