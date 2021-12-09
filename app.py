from flask import Flask, render_template, flash, redirect, url_for, request, session
from flask.helpers import url_for
# from flask_restful import Api, Resource
from forms import LoginForm, RegisterForm, UpdateProfileDetailsForm, DoctorRegisterForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models.doctor import Doctor

from models.patient import Patient
from models.userProfile import UserProfile
from models.user import User

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

# api = Api(app)

# class App(Resource):
#     def get(self):
#         # user_list = UserProfile.get_all_users()
#         # for idx in range(len(user_list)):
#         #     user_list[idx] = user_list[idx].__dict__
#         #     del user_list[idx]['_id']
#         # return user_list
#         auth_status = User.login('1234', '15-08-2000')
#         return auth_status

#     def post(self):
#         user = User('abc', '1234', '1234567890', '15-08-2000', True, False)

#         user.save()
        
#         desired_profile = UserProfile.find_user_by_id('1234')

#         return desired_profile.__dict__

# api.add_resource(App, '/')

@login_manager.user_loader
def load_user(user_id):
    return User.find_by_id(user_id)

############################# Home Page ##############################

@app.route('/') # Home Page --> 127.0.0.1:5000/
def index():
    
    return render_template('home.html')

############################# Authentication ##############################

@app.route('/authenticate/login', methods=["GET", "POST"]) # Login Page --> 127.0.0.1:5000/authenticate/login
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        # TODO: Login the user
        national_id = login_form.national_id.data
        dob = login_form.dob.data
        user = User.find_by_id(national_id)
        print(user)
        if not user or not user.dob == dob:
            flash('Please check the login credentials adn try again!')
            return redirect('login')
        login_user(user)
        flash('Log in successful!')
        return redirect(url_for('profile'))


    return render_template('authentication/login.html', login_form=login_form)

@app.route('/authenticate/regiter', methods=["GET", "POST"]) # Register Page --> 127.0.0.1:5000/authenticate/register
def register():
    register_form = RegisterForm()

    if register_form.validate_on_submit():

        name = register_form.name.data
        national_id = register_form.national_id.data
        phone_no = register_form.phone_no.data
        dob = register_form.dob.data
        
        user = User(name, national_id, phone_no, dob, False, False)

        user.save()
        flash('registration successful')
        return redirect(url_for('index'))

    return render_template('authentication/register.html', register_form=register_form)

@app.route('/authenticate/regiter/doctor', methods=["GET", "POST"]) # Register Page --> 127.0.0.1:5000/authenticate/register
def register_doctor():
    doctor_register_form = DoctorRegisterForm()

    if doctor_register_form.validate_on_submit():

        name = doctor_register_form.name.data
        national_id = doctor_register_form.national_id.data
        phone_no = doctor_register_form.phone_no.data
        dob = doctor_register_form.dob.data
        specialization = doctor_register_form.specialization.data
        location = doctor_register_form.location.data
        
        user = User(name, national_id, phone_no, dob, True, False)
        user.save()

        doctor = Doctor(user, specialization, location)
        doctor.save()

        flash('registration successful')
        return redirect(url_for('index'))

    return render_template('authentication/registerDoctor.html', doctor_register_form=doctor_register_form)


@app.route('/authenticate/logout')
@login_required
def logout():
    logout_user()
    flash('Logout successful!')
    return redirect(url_for('index'))

############################# Profile ##############################

@app.route('/my-profile', methods=["GET", "POST"])
@login_required
def profile():
    user_profile = UserProfile.find_user_by_id(current_user.national_id)

    if request.method == 'POST':
        req = request.form
        user_id = req.get('user_id')
        session['current_patient_id'] = user_id
        print(user_id)
        user_profile = UserProfile.find_user_by_id(user_id)
        print(user_profile.name)
        return render_template('profile/dashboard.html', user_profile = user_profile)

    return render_template('profile/dashboard.html', user_profile = user_profile)

@app.route('/my-profile/update', methods=["GET", "POST"])
@login_required
def update_my_profile():
    profile_updation_form = UpdateProfileDetailsForm()

    if request.method == 'GET':
        profile_updation_form.name.data = current_user.name
        profile_updation_form.national_id.data = current_user.national_id
        profile_updation_form.phone_no.data = current_user.phone_no
        profile_updation_form.dob.data = current_user.dob

    if profile_updation_form.validate_on_submit() and request.method == 'POST':

        name = profile_updation_form.name.data
        national_id = profile_updation_form.national_id.data
        phone_no = profile_updation_form.phone_no.data
        dob = profile_updation_form.dob.data

        print(name, national_id, phone_no, dob)
        current_user_id = current_user.national_id
        logout_user()
        User.update_user_details(current_user_id, name=name, national_id=national_id, phone_no=phone_no, dob=dob)

        return redirect(url_for('index'))

    return render_template('profile/updateProfileDetailsUpdate.html', profile_updation_form=profile_updation_form)

if __name__ == '__main__':
    app.run(debug=True, port=5000)