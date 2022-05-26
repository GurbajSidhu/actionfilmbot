from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("whats your favourite movie?"):
        return "The Good, The Bad, and The Ugly. \n\nGood old classic wild west action... They don't make them like that no more. \n\nSo, what brings you here? \n\nWanna look up a Movie? An Actor? I got it all as long as it is Action!"

    if user_message in ("kill bill"):
        return "'After awakening from a four-year coma, a former assassin wreaks vengeance on the team of assassins who betrayed her.' \n\nthe Best Action movie ever made - fight scenes evolved since Day One of Kung Fu movies, sword fights like you didn't think it was possible \n\nWanta look up another one?"

    if user_message in ("grindhouse"):
        return "Quentin Tarantino and Robert Rodriguez's homage to exploitation double features in the '60s and '70s with two back-to-back cult films that include previews of coming attractions between them."

    if user_message in ("from dusk till dawn"):
        return "Two criminals and their hostages unknowingly seek temporary refuge in a truck stop populated by vampires, with chaotic results."

    if user_message in ("the terminator"):
        return "A human soldier is sent from 2029 to 1984 to stop an almost indestructible cyborg killing machine, sent from the same year, which has been programmed to execute a young woman whose unborn son is the key to humanity's future salvation. \n\nGood Ol' KAPOW! KAPOW! movie from Arnold. \n\n I see you got good taste."

    if user_message in ("the matrix"):
        return ("When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence. \n\n Funny how the world has come resemble this movie recently. Crazy times.")

    if user_message in ("aliens"):
        return "Adventurer Lara Croft goes on a quest to save the mythical Pandora's Box, before an evil scientist finds it, and recruits a former Marine turned mercenary to assist her. \n\n That lass packs a punch!"

    if user_message in ("keanu reeves"):
        return "'Born 	September 2, 1964 in Beirut, Lebanon\n\nBirth Name	Keanu Charles Reeves \n\nNicknames	The Wall, The One\n\nIn my oppinion, The Matrix (1999) is his best work.'"

    if user_message in ("arnold"):
        return "Born 	July 30, 1947 in Thal, Styria, Austria\n\nBirth Name	Arnold Alois Schwarzenegger\n\nicknames	Arnie, Austrian Oak, Conan the Republican, Styrian Oak, The Machine\n\n Schwarzenegger dominated the sport of competitive bodybuilding winning five Mr. Universe titles and seven Mr. Olympia titles and, with it, he made himself a major sports icon\n\n THen he did awesome movies. Tough bloke. "

    if user_message in ("bye"):
        return "Goodbye, Ol' Sport. Keep kicking. Sayonara"

    return ("I haven't watched that one. I told you I only watch good movies.")
