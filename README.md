# Django Appointment Booking System with Mock Stripe Payment

A full-featured appointment booking system built with Django, featuring a mock Stripe payment integration for a complete booking experience.

## 🚀 Features

### Core Functionality
- **Appointment Booking**: Complete appointment scheduling system
- **Mock Stripe Payment**: Professional payment form with validation
- **Admin Dashboard**: View and manage all appointments
- **Responsive Design**: Works on desktop and mobile devices
- **Email Integration**: Ready for email notifications

### Payment System
- **Mock Stripe Integration**: Realistic payment form design
- **Service-Based Pricing**: Different prices for different services
- **Payment Validation**: Card number formatting and validation
- **Payment Success**: Confirmation page with payment details
- **Status Management**: Automatic appointment status updates

### Technical Features
- **Django 5.2**: Latest Django framework
- **SQLite Database**: Easy development setup
- **Bootstrap 5**: Modern, responsive UI
- **Template Inheritance**: Clean, maintainable templates
- **Form Validation**: Comprehensive form handling

## 📋 Services & Pricing

| Service | Price | Description |
|---------|-------|-------------|
| Consultation | $50.00 | Initial consultation and assessment |
| Cleaning | $150.00 | Deep cleaning service |
| Repair | $300.00 | Repair and maintenance work |
| Maintenance | $75.00 | Regular maintenance service |

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- Django 5.2+
- Git

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-github-repo-url>
   cd appointment
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

7. **Open browser and visit**
   ```
   http://127.0.0.1:8000/
   ```

## 📁 Project Structure

```
appointment/
├── manage.py                 # Django project manager
├── mysite/                   # Main Django project
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── appointments/             # Main app
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── forms.py             # Django forms
│   ├── urls.py              # App URL patterns
│   ├── apps.py              # App configuration
│   └── templates/
│       └── appointments/
│           ├── appointment_form.html     # Booking form
│           ├── payment.html              # Payment form
│           ├── payment_success.html      # Payment confirmation
│           └── appointment_list.html     # Admin dashboard
├── db.sqlite3               # Database file
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🌐 URL Patterns

| URL | View | Description |
|-----|------|-------------|
| `/` | Root redirect | Redirects to booking form |
| `/book/` | Appointment form | Book new appointment |
| `/checkout/<id>/` | Payment form | Process payment |
| `/process-payment/<id>/` | Payment processing | Handle payment |
| `/payment-success/<id>/` | Payment success | Show confirmation |
| `/appointments/` | Admin dashboard | View all appointments |
| `/admin/` | Django admin | Admin interface |

## 💳 Payment Flow

1. **Appointment Booking** (`/book/`)
   - User fills appointment details
   - Form validation
   - Redirect to payment

2. **Payment Processing** (`/checkout/<id>/`)
   - Display service pricing
   - Mock Stripe payment form
   - Card validation and formatting

3. **Payment Confirmation** (`/payment-success/<id>/`)
   - Payment success message
   - Appointment confirmation
   - Next steps for user

## 🎨 UI Features

### Design Elements
- **Modern Interface**: Clean, professional design
- **Responsive Layout**: Works on all screen sizes
- **Bootstrap Integration**: Consistent styling
- **Interactive Forms**: Real-time validation
- **Loading States**: Visual feedback during processing

### Templates
- **Base Template**: Common layout and navigation
- **Form Templates**: User-friendly input forms
- **Success Pages**: Confirmation and next steps
- **Admin Interface**: Management dashboard

## 🔧 Configuration

### Settings
- **DEBUG**: Set to `True` for development
- **SECRET_KEY**: Unique Django secret key
- **ALLOWED_HOSTS**: Configure for production
- **Database**: SQLite for development, PostgreSQL for production

### Security
- **CSRF Protection**: Enabled on all forms
- **Secure Headers**: Security middleware configured
- **Password Validation**: Django's built-in validators

## 🚀 Deployment Options

### Recommended Platforms for Django
- **Vercel**: Serverless Django deployment (with vercel.json)
- **Heroku**: Easy Django deployment
- **PythonAnywhere**: Free Python hosting
- **Railway**: Modern deployment platform
- **Render**: Fast, free Django hosting
- **DigitalOcean App Platform**: Scalable deployment

### Vercel Deployment (Serverless)
1. **Connect GitHub repository** to Vercel
2. **Automatic deployment** on every push
3. **Environment variables** configured in Vercel dashboard
4. **Database** uses Vercel Postgres or external provider
5. **Static files** handled automatically

### Production Deployment
1. Set `DEBUG = False`
2. Configure `ALLOWED_HOSTS`
3. Set up production database
4. Configure static files
5. Set up email backend

## 📊 Database Models

### Appointment Model
- **Customer Information**: Name, email, phone
- **Appointment Details**: Date, time, service type
- **Additional Info**: Notes, status
- **Timestamps**: Created and updated dates

## 🔒 Security Features

- **Form Validation**: Server-side validation
- **CSRF Protection**: Cross-site request forgery prevention
- **Secure Headers**: Security middleware
- **Input Sanitization**: Safe form handling
- **SQL Injection Prevention**: Django ORM protection

## 🧪 Testing

### Manual Testing
1. Create appointments with different services
2. Test payment flow with mock card details
3. Verify admin dashboard functionality
4. Test responsive design on mobile devices

### Mock Payment Testing
- **Card Number**: `1234 5678 9012 3456`
- **Expiry**: `12/25`
- **CVC**: `123`
- **Name**: Any valid name

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🆘 Support

For support and questions:
- Create an issue on GitHub
- Check the Django documentation
- Review the code comments

## 🎯 Next Steps

### Potential Enhancements
- **Real Stripe Integration**: Connect to actual Stripe API
- **Email Notifications**: Automated email confirmations
- **Calendar Integration**: Google Calendar or Outlook sync
- **SMS Notifications**: Text message reminders
- **Admin Features**: Advanced appointment management
- **Reporting**: Analytics and reporting dashboard

### Production Ready Features
- **Error Monitoring**: Sentry or similar service
- **Backup System**: Database backups
- **Performance Optimization**: Caching and optimization
- **Security Hardening**: Production security measures

---

**Built with ❤️ using Django 5.2**