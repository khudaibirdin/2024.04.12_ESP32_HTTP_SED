css = """
* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}
body {
    background-color: #F5F5F5;
    font-family: sans-serif;
    display: flex;
    flex-direction: column;
    text-align: center;
    justify-content: center;
}
.block_head {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 24px;
    font-weight: 800;
    height: 50px;
    background-color:black;
    color:white;
    margin-bottom: 20px;
}
.block_body {
    display: flex;
    flex-direction: column;
    font-size: 20px;
    font-weight: 400;
    margin: auto;
    gap: 5px;
}
.block_body div {
    display: flex;
    gap: 10px;
    padding: 5px;
}
.block_body p {
    display: flex;
    gap: 10px;
    align-items: center;
}

.switch {
    position: relative;
    display: inline-block;
    width: 60px;
    height: 34px;
  }
  
  /* Скрыть флажок HTML по умолчанию */
  .switch input {
    opacity: 0;
    width: 0;
    height: 0;
  }
  
  /* Ползунок */
  .slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #ccc;
    -webkit-transition: .4s;
    transition: .4s;
  }
  
  .slider:before {
    position: absolute;
    content: "";
    height: 26px;
    width: 26px;
    left: 4px;
    bottom: 4px;
    background-color: white;
    -webkit-transition: .4s;
    transition: .4s;
  }
  
  input:checked + .slider {
    background-color: black;
  }
  
  input:focus + .slider {
    box-shadow: 0 0 1px #2196F3;
  }
  
  input:checked + .slider:before {
    -webkit-transform: translateX(26px);
    -ms-transform: translateX(26px);
    transform: translateX(26px);
  }
  
  /* Закругленные ползунки */
  .slider.round {
    border-radius: 34px;
  }
  
  .slider.round:before {
    border-radius: 50%;
  }
"""

html= """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=0.8">
    <title>Веб-освещение</title>
    <style>%s</style>
</head>
<body>
    <div class="block_head">
        Освещение v0.1
    </div>
    <div class="block_body">
        <form method="get">
        <div>
            <p>Идентификация устройства</p>
            <p><input type="checkbox" name="identification_auto" value="checked" %s></p><p style="font-size: 14px;">Авто</p>
        </div>
        <div>
            <p><input type="text" name="code" value="%s"></p><p style="font-size: 14px;"></p>
            
        </div>
        <div>
            <p>Режим работы</p>
            <p><input type="checkbox" name="regime" value="checked" %s></p><p style="font-size: 14px;">Ежесуточно</p>
        </div>
        <div>
            <p><input type="time" name="on_time" value="checked" %s></p>
            <p style="font-size: 14px;"> Время включения</p>
        </div>
        <div>
            <p><input type="time" name="work_period" value="checked" %s></p>
            <p style="font-size: 14px;"> Продолжительность работы</p>
        </div>
        <div>
            <!--<p><input type="range" name="brightness" step="10" min="30" max="100" value="50" style="accent-color: black;"></p>-->
            <p><input type="number" name="brightness" step="10" min="30" max="100" value="%s" style="width: 50px;"></p>
            <p style="font-size: 14px;">Яркость (30-100%%)</p>
        </div>
        <div style="justify-content: center;">
            <label class="switch">
                <input type="checkbox" name=manual value="checked" %s>
                <span class="slider round"></span>
            </label>
        </div>
        <div style="flex-direction: column; font-size: 14px;">
            <p>Демонстрационный режим работы</p>
            <p>
                <input type="radio" value="1" %s name="demo_type"/>100%%, 30 c
            </p>
            <p>
                <input type="radio" value="2" %s name="demo_type"/>100%%, 30 c; 50%%, 30 c; 100%%, 45 c
            </p>
            <p>
                <input type="radio" value="3" %s name="demo_type"/>100%%, 20 c; 70%%, 30 c
            </p>
            <p>
                <input type="radio" value="4" %s name="demo_type"/>100%%, 20 c; 50%%, 15 c; 20%% 15 c; 100%%, 15c
            </p>
            <p>
                <input type="radio" value="5" %s name="demo_type"/>100%%, 30 c; 50%%, 15 c
            </p>
        </div>
        <div style="justify-content: center;">
            <label class="switch" >
                <input type="checkbox" name=demo value="checked" %s>
                <span class="slider round"></span>
            </label>
        </div>
        <div style="justify-content: center;">
            <p><button type="submit" name="confirm" style="height: 40px; width: 150px; font-size: 14px; color: white; background-color: black; padding: 4px; border: 0px; border-radius: 5px;">Обновить</button></p>
        </div>
        </form>
    </div>
</body>
</html>

"""

