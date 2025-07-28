from flask import Flask, render_template, request, redirect, url_for
from models import db, DevOpsTool, PendingTopic
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    tools = DevOpsTool.query.all()
    return render_template('index.html', tools=tools)

@app.route('/add_tool', methods=['GET', 'POST'])
def add_tool():
    if request.method == 'POST':
        tool_name = request.form['tool_name']
        status = request.form['status']
        completion_percent = request.form.get('completion_percent', None)
        
        new_tool = DevOpsTool(
            tool_name=tool_name,
            status=status,
            completion_percent=completion_percent if status in ['pending', 'revision'] else None
        )
        
        db.session.add(new_tool)
        db.session.commit()
        
        # Add pending topics if status requires it
        if status in ['pending', 'revision']:
            topics = request.form.getlist('pending_topics')
            for topic in topics:
                if topic.strip():  # Skip empty topics
                    new_topic = PendingTopic(topic=topic, tool_id=new_tool.id)
                    db.session.add(new_topic)
        
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('add_tool.html')

@app.route('/update_status/<int:tool_id>', methods=['POST'])
def update_status(tool_id):
    tool = DevOpsTool.query.get_or_404(tool_id)
    new_status = request.form['status']
    
    tool.status = new_status
    if new_status in ['pending', 'revision']:
        tool.completion_percent = request.form.get('completion_percent', 0)
    else:
        tool.completion_percent = None
    
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,host='0.0.0.0')
