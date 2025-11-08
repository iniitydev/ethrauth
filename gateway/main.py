from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

import httpx
from fastapi import Body

...

@app.post("/onboard-user")
async def onboard_user(data: dict = Body(...)):
    email = data.get("email")
    if not email:
        return {"error": "Email is required"}, 400

    async with httpx.AsyncClient() as client:
        # 1. Create user in Zitadel
        zitadel_response = await client.post(
            "http://zitadel:8080/management/v1/users",
            json={"email": email, "userName": email.split('@')[0]},
            headers={"Authorization": "Bearer YOUR_ZITADEL_TOKEN"}
        )

        # 2. Create setup key in NetBird
        netbird_response = await client.post(
            "http://netbird-management:33073/api/setup-keys",
            json={"name": f"key-{email}", "ephemeral": True},
            headers={"Authorization": "Bearer YOUR_NETBIRD_TOKEN"}
        )

        # 3. Create user in Nextcloud
        nextcloud_response = await client.post(
            "http://nextcloud/ocs/v1.php/cloud/users",
            data={"userid": email.split('@')[0], "password": "a-secure-password"},
            auth=("admin", "YOUR_NEXTCLOUD_ADMIN_PASSWORD"),
            headers={"OCS-APIRequest": "true"}
        )

    return {
        "message": "User onboarding process initiated.",
        "zitadel_status": zitadel_response.status_code,
        "netbird_status": netbird_response.status_code,
        "nextcloud_status": nextcloud_response.status_code
    }

@app.get("/user/{user_id}")
async def get_user(user_id: str):
    async with httpx.AsyncClient() as client:
        # 1. Get user from Zitadel
        zitadel_response = await client.get(
            f"http://zitadel:8080/management/v1/users/{user_id}",
            headers={"Authorization": "Bearer YOUR_ZITADEL_TOKEN"}
        )

        # 2. Get peers from NetBird
        netbird_response = await client.get(
            f"http://netbird-management:33073/api/peers?user_id={user_id}",
            headers={"Authorization": "Bearer YOUR_NETBIRD_TOKEN"}
        )

        # 3. Get user from Nextcloud
        nextcloud_response = await client.get(
            f"http://nextcloud/ocs/v1.php/cloud/users/{user_id}",
            auth=("admin", "YOUR_NEXTCLOUD_ADMIN_PASSWORD"),
            headers={"OCS-APIRequest": "true"}
        )

    return {
        "zitadel_user": zitadel_response.json(),
        "netbird_peers": netbird_response.json(),
        "nextcloud_user": nextcloud_response.json()
    }
