from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/projects')
def projects():
    projects_data = [
        {
            'id': 1,
            'name': 'AURA – AI Personal Voice Assistant',
            'description': 'An intelligent voice-based AI assistant built using Python that can understand natural speech, answer general and complex questions, adapt to user preferences, and perform automated system tasks. Modeled to think, learn, and communicate like a human, AURA integrates speech recognition, NLP, and dynamic knowledge retrieval to provide context-aware and accurate responses.',
            'technologies': ['Python', 'Django', 'PyAudio', 'SpeechRecognition', 'Transformers', 'Wikipedia API', 'Wikidata API', 'Torch', 'gTTS'],
            'status': 'In-Development',
            'github': 'https://github.com/VirajGhadge'
        },
        {
            'id': 2,
            'name': 'Student Performance Tracking System',
            'description': 'A comprehensive full-stack application for managing and analyzing student academic performance. Features include student/course management, marks recording, automated grade calculation, performance reporting, and class analytics. Built with dual interfaces (Console CLI + Modern Web UI) using a single SQLite3 database for data persistence.',
            'technologies': ['Python', 'Flask', 'SQLite3', 'HTML5', 'CSS3', 'JavaScript', 'RESTful API', 'AJAX'],
            'status': 'In-Development',
            'github': 'https://github.com/VirajGhadge'
        }
    ]
    return render_template('projects.html', projects=projects_data)

@main_bp.route('/blog')
def blog():
    blog_posts = [
        {
            'id': 1,
            'title': 'The Journey of Building AURA: Lessons in AI and Python',
            'excerpt': 'Explore the technical challenges and breakthroughs in creating an intelligent voice assistant...',
            'content': '''The journey of building AURA has been an exciting exploration into the world of artificial intelligence and natural language processing. From the initial spark of an idea to implementing complex voice recognition algorithms, every step taught me something new about Python's capabilities and the power of open-source libraries.

The most challenging part was integrating multiple APIs and ensuring seamless communication between different components. Working with Hugging Face Transformers, Wikipedia APIs, and text-to-speech engines required careful orchestration and error handling.

One key lesson I learned: always prioritize user experience. The AI model might be brilliant, but if it doesn't understand the user's intent correctly, it fails. This led me to implement context awareness and adaptive learning features that make AURA more intuitive with each interaction.

Looking back, I realize that building AI assistants is not just about coding—it's about understanding human communication patterns and creating bridges between machines and people.'''
        },
        {
            'id': 2,
            'title': 'Full-Stack Development: From Concept to Deployment',
            'excerpt': 'A deep dive into building the Student Performance Tracking System and lessons learned...',
            'content': '''Full-stack development is an art of balancing frontend aesthetics with backend efficiency. While building the Student Performance Tracking System, I discovered that the best applications are those that seamlessly blend powerful databases with intuitive user interfaces.

The project taught me the importance of proper database design and normalization. Using SQLite3 with proper foreign keys and constraints ensured data integrity across the entire system. Meanwhile, the frontend needed to be responsive and engaging to encourage actual usage.

One interesting decision was to provide both CLI and web interfaces. This dual-interface approach catered to different user preferences—power users loved the CLI for quick operations, while administrators preferred the web UI for comprehensive analytics.

The REST API design was crucial in making the backend flexible and scalable. Using AJAX for dynamic content updates made the web interface feel modern and responsive without full page reloads.

Key takeaway: Great full-stack applications are built on strong fundamentals—clean architecture, proper database design, and user-centric interface design.'''
        }
    ]
    return render_template('blog.html', blog_posts=blog_posts)
