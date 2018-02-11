from flask import Flask, render_template, request
import configparser

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        update_config(request.form)
    sensor_list = [sensor for sensor in app.config["PW_CONFIG"] if
                   sensor != "PLAYWEATHER_STATION" and sensor != "DEFAULT"]
    return render_template('index.html', sensors=sensor_list, config=app.config['PW_CONFIG'])

@app.route('/restart')
def restart():
    # do something here
    return "Restart not implemented"


def update_config(form):
    form = form.to_dict()
    with open('config.ini', 'w') as configfile:
        config["PLAYWEATHER_STATION"]["id"] = form.pop('station-id')
        config["PLAYWEATHER_STATION"]["delivery_interval"] = form.pop("delivery-interval")

        for sensor in {sensor.replace("-id", "").replace("-collection-interval", "") for sensor in form}:
            config[sensor]['id'] = form[sensor + '-id']
            config[sensor]['collection_interval'] = form[sensor + '-collection-interval']

        config.write(configfile)

    return 'Done'


def get_pw_config_value(key):
    return app.config['PW_CONFIG']['DEFAULT'][key]


def init(pw_instance):
    app.config['PW_INSTANCE'] = pw_instance
    app.config['PW_CONFIG'] = app.config['PW_INSTANCE'].config

    app.run()


def default_config():
    new_config = configparser.ConfigParser()
    new_config["PLAYWEATHER_STATION"] = {
        "id": "station",
        "delivery_interval": "5",
    }
    return new_config


def validate(config):
    if "PLAYWEATHER_STATION" not in config:
        return False
    if "id" not in config["PLAYWEATHER"]:
        return False
    return True


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    with open('config.ini', 'w') as configfile:
        config["PLAYWEATHER_STATION"] = {
            "id": "pw_station",
            "delivery_interval": "12"
        }
        config["CO"] = {
            "id": "co",
            "collection_interval": "3"
        }

        config.write(configfile)

    app.config['PW_CONFIG'] = config

    print(app.config['PW_CONFIG'])
    app.run()