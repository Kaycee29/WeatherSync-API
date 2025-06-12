resource "aws_s3_bucket" "weather-api-extracts"{
  bucket = "weather-api-kaycee2025"

  tags = {
    Name        = "weather-extracts"
    Environment = "production"
  }
}

# create IAM user

resource "aws_iam_user" "kaycee-user" {
  name = "kaycee"
}

resource "aws_iam_access_key" "access-key" {
  user = aws_iam_user.kaycee-user.name
}

resource "aws_iam_user_policy" "kaycee_policy" {
  name = "kaycee-user-policy"
  user = aws_iam_user.kaycee-user.name

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = [
          "s3:ListAllBuckets",
        ],
        Effect   = "Allow",
        Resource = "*"
      },
      {
        Action = [
          "s3:PutObject",
          "s3:DeleteObject",
        ],
        Effect   = "Allow",
        Resource = "arn:aws:s3:::weather-api-kaycee2025/*"
      }
    ]
  })
}

resource "aws_ssm_parameter" "kaycee_access" {
  name  = "kaycee_access"
  type  = "String"
  value = aws_iam_access_key.access-key.id
}
resource "aws_ssm_parameter" "kaycee_secret" {
  name  = "kaycee_secret"
  type  = "String"
  value = aws_iam_access_key.access-key.secret
}