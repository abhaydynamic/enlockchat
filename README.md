# 🔒 Enlock Chat - Secure End-to-End Encrypted Messaging

<div align="center">
  <img src="static/logo.svg" alt="Enlock Chat Logo" width="120" height="120">
  
  **Privacy-first messaging with end-to-end encryption, voice messages, and real-time communication**
  
  [![PWA Ready](https://img.shields.io/badge/PWA-Ready-brightgreen.svg)](https://developers.google.com/web/progressive-web-apps/)
  [![Firebase](https://img.shields.io/badge/Firebase-Powered-orange.svg)](https://firebase.google.com/)
  [![Flask](https://img.shields.io/badge/Flask-Python-blue.svg)](https://flask.palletsprojects.com/)
  [![End-to-End Encryption](https://img.shields.io/badge/E2EE-AES--GCM-red.svg)](https://en.wikipedia.org/wiki/Galois/Counter_Mode)
</div>

## 🌟 Features

### 🔐 Security & Privacy
- **End-to-End Encryption**: AES-GCM 256-bit encryption for all messages
- **Zero-Knowledge Architecture**: Messages encrypted client-side
- **Secure Authentication**: Firebase Auth with email/password
- **Privacy Controls**: Block/unblock users, message deletion
- **Local Key Storage**: Encryption keys never leave your device

### 💬 Messaging Features
- **Real-time Messaging**: Instant message delivery with Firebase
- **Voice Messages**: Record and send encrypted voice notes
- **File Sharing**: Secure file uploads with encryption
- **Message Reactions**: React with emojis to messages
- **Message Editing**: Edit sent messages with history tracking
- **Message Forwarding**: Forward messages to multiple contacts
- **Reply System**: Reply to specific messages with threading
- **Message Search**: Search through conversation history
- **Message Pinning**: Pin important messages for easy access
- **Typing Indicators**: See when others are typing
- **Read Receipts**: Message delivery and read status
- **Link Previews**: Rich previews for shared URLs

### 🎨 User Experience
- **Dark/Light Mode**: Toggle between themes with system preference
- **Responsive Design**: Perfect on mobile, tablet, and desktop
- **Progressive Web App**: Install as native app on any device
- **Offline Support**: Continue using app without internet
- **Real-time Updates**: Live message synchronization
- **Emoji Picker**: Rich emoji selection for reactions
- **File Drag & Drop**: Easy file sharing with drag and drop
- **Mobile Optimized**: Touch-friendly interface for mobile devices

## 📱 Progressive Web App (PWA)

Enlock Chat is a full-featured Progressive Web App that provides:

- **📲 Installable**: Add to home screen on mobile/desktop
- **⚡ Fast Loading**: Service worker caching for instant startup
- **🔄 Offline Mode**: Continue chatting even without internet
- **🔔 Push Notifications**: Real-time message notifications
- **📊 App-like Experience**: Native app feel in the browser
- **🔄 Auto-Updates**: Seamless app updates in background

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Firebase project with Firestore and Storage enabled
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd chat-app
   ```

2. **Install dependencies**
   ```bash
   pip install Flask
   ```

3. **Firebase Setup**
   - Create a Firebase project at [Firebase Console](https://console.firebase.google.com/)
   - Enable Firestore Database
   - Enable Firebase Storage
   - Enable Authentication (Email/Password)
   - Copy your Firebase config

4. **Configure Firebase**
   - Replace the Firebase config in `templates/chat_fixed.html` with your project's config:
   ```javascript
   const firebaseConfig = {
     apiKey: "your-api-key",
     authDomain: "your-project.firebaseapp.com",
     projectId: "your-project-id",
     // ... other config
   };
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   - Navigate to `http://127.0.0.1:5000/`
   - Create an account or sign in
   - Start chatting securely!

## 🔧 Configuration

### Firebase Rules

Configure Firestore security rules for proper access control:

```javascript
// Firestore Rules
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Users can read/write their own user document
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
    
    // Chat messages - users can only access chats they're part of
    match /chats/{chatId}/messages/{messageId} {
      allow read, write: if request.auth != null && 
        request.auth.uid in resource.data.participants;
    }
    
    // Chat metadata
    match /chatMetadata/{chatId} {
      allow read, write: if request.auth != null && 
        request.auth.uid in resource.data.participants;
    }
  }
}
```

### Storage Rules

Configure Firebase Storage rules for file uploads:

```javascript
// Storage Rules
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /chat-files/{userId}/{allPaths=**} {
      allow read, write: if request.auth != null && 
        request.auth.uid == userId;
    }
  }
}
```

## 🏗️ Architecture

### Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend**: Python Flask
- **Database**: Firebase Firestore (NoSQL)
- **Storage**: Firebase Storage
- **Authentication**: Firebase Auth
- **Encryption**: Web Crypto API (AES-GCM)
- **UI Framework**: Tailwind CSS
- **Icons**: Font Awesome
- **PWA**: Service Worker, Web App Manifest

### Security Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Client App    │    │   Firebase      │    │   Encryption    │
│                 │    │                 │    │                 │
│ ┌─────────────┐ │    │ ┌─────────────┐ │    │ ┌─────────────┐ │
│ │ Message UI  │ │    │ │ Firestore   │ │    │ │ AES-GCM     │ │
│ └─────────────┘ │    │ │ Database    │ │    │ │ 256-bit     │ │
│ ┌─────────────┐ │    │ └─────────────┘ │    │ └─────────────┘ │
│ │ Crypto API  │◄┼────┼►┌─────────────┐ │    │ ┌─────────────┐ │
│ └─────────────┘ │    │ │ Auth        │ │    │ │ Local Keys  │ │
│ ┌─────────────┐ │    │ └─────────────┘ │    │ └─────────────┘ │
│ │ Service     │ │    │ ┌─────────────┐ │    │                 │
│ │ Worker      │ │    │ │ Storage     │ │    │                 │
│ └─────────────┘ │    │ └─────────────┘ │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 📁 Project Structure

```
chat-app/
├── 📄 app.py                 # Flask application server
├── 📄 README.md             # Project documentation
├── 📄 FIREBASE_RULES.md     # Firebase security rules
├── 📄 FIREBASE_STORAGE_RULES.md # Storage security rules
├── 📁 static/               # Static assets
│   ├── 🖼️ logo.svg          # App logo (SVG)
│   ├── 🖼️ logo.png          # App logo (PNG)
│   ├── 📄 manifest.json     # PWA manifest
│   └── 📄 sw.js             # Service worker
└── 📁 templates/            # HTML templates
    └── 📄 chat_fixed.html   # Main chat interface
```

## 🛡️ Security Features

### Encryption Details

- **Algorithm**: AES-GCM (Galois/Counter Mode)
- **Key Length**: 256 bits
- **Key Generation**: Web Crypto API `crypto.subtle.generateKey()`
- **Key Storage**: Browser's IndexedDB (never transmitted)
- **Message Encryption**: Client-side before transmission
- **File Encryption**: Files encrypted before upload

### Privacy Features

- **Zero-Knowledge**: Server never sees plaintext messages
- **Forward Secrecy**: New keys for each session
- **User Blocking**: Block unwanted contacts
- **Message Deletion**: Delete for self or everyone
- **Secure Authentication**: Firebase Auth integration
- **HTTPS Only**: All communications over HTTPS

## 📱 Mobile Features

### Touch Optimizations
- Touch-friendly message bubbles
- Swipe gestures for quick actions
- Mobile-optimized emoji picker
- Responsive file upload area
- Mobile keyboard support

### PWA Mobile Features
- Add to home screen
- Full-screen experience
- Offline message queue
- Push notifications
- Background sync

## 🔍 Browser Support

| Browser | Support | PWA Features |
|---------|---------|--------------|
| Chrome 80+ | ✅ Full | ✅ Complete |
| Firefox 75+ | ✅ Full | ⚠️ Limited |
| Safari 13+ | ✅ Full | ⚠️ Limited |
| Edge 80+ | ✅ Full | ✅ Complete |

## 🚀 Deployment

### Local Development
```bash
python app.py
# App runs on http://127.0.0.1:5000/
```

### Production Deployment

#### Option 1: Heroku
```bash
# Create Procfile
echo "web: python app.py" > Procfile

# Create requirements.txt
echo "Flask==2.3.3" > requirements.txt

# Deploy to Heroku
heroku create your-app-name
git push heroku main
```

#### Option 2: Railway
```bash
# Connect GitHub repo to Railway
# Set environment variables
# Deploy automatically
```

#### Option 3: Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow Python PEP 8 style guide
- Add comments for complex encryption logic
- Test PWA features on multiple devices
- Ensure mobile responsiveness
- Maintain security best practices

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Firebase** for real-time database and authentication
- **Web Crypto API** for client-side encryption
- **Tailwind CSS** for responsive design
- **Font Awesome** for beautiful icons
- **PWA** community for progressive web app standards

## 📞 Support

- 📧 Email: support@enlock-chat.com
- 🐛 Issues: [GitHub Issues](https://github.com/your-repo/issues)
- 📖 Documentation: [Wiki](https://github.com/your-repo/wiki)
- 💬 Community: [Discord Server](https://discord.gg/your-server)

## 🔮 Roadmap

### Upcoming Features
- [ ] Group chat functionality
- [ ] Video calling integration
- [ ] Message scheduling
- [ ] Custom themes
- [ ] Desktop notifications
- [ ] Message backup/export
- [ ] Multi-device synchronization
- [ ] Advanced admin controls

---

<div align="center">
  <strong>Built with ❤️ for privacy and security</strong>
  
  Made by developers who believe in digital privacy rights
</div>
