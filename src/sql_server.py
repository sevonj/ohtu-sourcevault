import boto3


class ServerHandler:
    """
    Kommunikoi AWS-pilvipalvelun kanssa.
    ...

    Parameters
    ----------
    aws_key, aws_secret_key : str
        Avaimet jotka vaaditaan pilvipalvelun kanssa kommunikointiin.
    local_db : str
        Minne tallennetaan.
    remote_db : str
        Tietokannan nimi pilvipalvelussa.
    bucket_name : str
        AWS-bucket, johon tietokanta on tallennettu.

    Methods
    -------
    get_references():
        Hakee tietokannan AWS-pilvipalvelusta.
    upload_references():
        Tallentaa tietokannan AWS-pilvipalveluun.
    """
    def __init__(self, aws_key, aws_secret_key, local_db, remote_db, bucket_name):
        self.local_db = local_db
        self.remote_db = remote_db
        self.bucket_name = bucket_name
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=aws_key,
            aws_secret_access_key=aws_secret_key,
            region_name='eu-north-1'
            )
        
    def get_references(self):
        self.s3.download_file(self.bucket_name, self.remote_db, self.local_db)

    def upload_references(self):
        self.s3.upload_file(self.local_db, self.bucket_name, self.remote_db)