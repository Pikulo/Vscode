from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

host_server = 'smtp.qq.com'
sender_qq = '2950771552@qq.com'
pwd = 'jcbpsluyprkoddic'
receiver = ['lmy15082035951@outlook.com']

mail_title = 'Python�Զ����͵��ʼ�'
mail_content = "���ã�����ʹ��python��¼QQ���䷢���ʼ��Ĳ��ԡ���zep"
# ��ʼ��һ���ʼ�����
msg = MIMEMultipart()
msg["Subject"] = Header(mail_title,'utf-8')
msg["From"] = sender_qq
# msg["To"] = Header("��������",'utf-8')
msg['To'] = ";".join(receiver)
# �ʼ���������
msg.attach(MIMEText(mail_content,'plain','utf-8'))



smtp = SMTP_SSL(host_server) # ssl��¼

# login(user,password):
# user:��¼������û�����
# password����¼��������룬������õ����������䣬��������һ������ҳ�棬��Ҫ�õ��ͻ������룬��Ҫ����ҳ�������������������Ȩ�룬����Ȩ�뼴Ϊ�ͻ������롣
smtp.login(sender_qq,pwd)

# sendmail(from_addr,to_addrs,msg,...):
# from_addr:�ʼ������ߵ�ַ
# to_addrs:�ʼ������ߵ�ַ���ַ����б�['���յ�ַ1','���յ�ַ2','���յ�ַ3',...]��'���յ�ַ'
# msg��������Ϣ���ʼ����ݡ�һ����msg.as_string():as_string()�ǽ�msg(MIMEText�������MIMEMultipart����)��Ϊstr��
smtp.sendmail(sender_qq,receiver,msg.as_string())

# quit():���ڽ���SMTP�Ự��
smtp.quit()