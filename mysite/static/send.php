<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'PHPMailer/src/Exception.php';
require 'PHPMailer/src/PHPMailer.php';
require 'PHPMailer/src/SMTP.php';

if (isset($_POST['name'])) {
    $name = $_POST['name'];
}
if (isset($_POST['phone'])) {
    $phone = $_POST['phone'];
}
if (isset($_POST['mmail'])) {
    $mmail = $_POST['mmail'];
}

$email = "udarnik.kirill@mail.ru";
$to = "sand@sandco.kz";

$sub = "Заявка с сайта Sandco.kz";

$mes = "<b>$sub</b><br><br>
        <b>Имя:</b> $name <br>
        <b>Телефон:</b> $phone <br>
        <b>E-mail:</b> $mmail";

$mail = new PHPMailer(true);

$mail->CharSet = 'UTF-8';

try {
    // Настройки SMTP
    $mail->isSMTP();
    $mail->Host = 'smtp.mail.ru'; // Укажите ваш SMTP-сервер
    $mail->SMTPAuth = true;
    $mail->Username = 'udarnik.kirill@mail.ru'; // Ваш SMTP username
    $mail->Password = 'xTvcJUYPeh8njBe4VY5F'; // Ваш SMTP пароль
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
    $mail->Port = 587; // Обычно порт для STARTTLS 587

    // Отправитель и получатели
    $mail->setFrom($email, 'Sandco.kz');
    $mail->addAddress($to);

    // Контент письма
    $mail->isHTML(true);
    $mail->Subject = $sub;
    $mail->Body = $mes;

    // Отправка письма
    $mail->send();
    header('Location: /company/');
} catch (Exception $e) {
    // echo "Ошибка отправки письма: {$mail->ErrorInfo}";
    header('Location: success/error.html');
}
?>
