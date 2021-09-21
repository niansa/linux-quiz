#include <stdio.h>
#include <stdint.h>
#include <unistd.h>

uint8_t answer_count = 0,
        question_count = 0;



char getchar_nl() {
    char fres = getchar();
    while (getchar() != '\n');
    return fres;
}

void question(const char *question_title, const char *answer_1, const char *answer_2, const char *answer_3, const char answer_right) {
    question_count++;
    printf("%u. %s\n", question_count, question_title);
    usleep(200000);
    printf("a) %s\nb) %s\nc) %s", answer_1, answer_2, answer_3);
    printf("\n ———> ");
    char answer_user = getchar_nl();
    if (answer_user == answer_right) {
        printf("Richtig\n");
        answer_count++;
    } else {
        printf("Falsch\n");
    }
    usleep(600000);
    printf("\033[2J\033[1;1H");
}

int main() {
    printf("Willkommen zum Linux Quiz. Du musst jetzt alle Fragen mit \"a\" \"b\" oder \"c\" beantworten. Um das Quiz zu starten, drücke Enter: ");
    getchar_nl();

    question("Was ist Linux?", "Eine Desktopumgebung", "Ein Kernel", "Ein Betriebssystem", 'b');
    question("Wie heißt das Maskottchen von Linux?", "Tuz", "Tux", "Tuc", 'b');
    question("Wer ist der Erfinder von Linux?", "Linus Torvalds", "Christiano Ronaldo", "Judd Vinet", 'a');
    question("Welche Distribution ist die älteste, die noch weiterentwickelt wird?", "Ubuntu", "OpenSuse", "Slackware", 'c');
    question("Welche Distribution basiert nicht auf Debian?", "Arch Linux", "Raspbian", "Ubuntu", 'a');
    question("Seit wann gibt es Linux?", "seit 1991", "seit 1985", "seit 2004", 'a');
    question("Unter welcher Lizenz wird Linux herausgegeben?", "Apache 2.0", "Mozilla Public Licence", "GPLv2", 'c');
    question("Welche dieser Distribution wird allgemein für Anfänger empfohlen?", "OpenSuse", "Linux Mint", "Kali Linux", 'b');
    question("Welcher Paketmanager wird bei der Distribution Fedora eingesetzt?", "apt", "zypper", "dnf", 'c');

    float ratio = answer_count / question_count;
    const char *result;
    if (ratio >= 0.8f) {
        result = "Super! Du scheinst dich echt sehr gut mit Linux auszukennen.";
    } else if (ratio >= 0.5f) {
        result = "Relativ gut! Hier und dort könntest du aber noch Wissenslücken füllen. ;)";
    } else {
        result = "Naja... Informiere dich eventuell noch einmal etwas mehr über Linux, und probiere es anschließend erneut. Denn Übung macht den Meister!";
    }

    printf("—————————————–\nDas Quiz ist zu Ende. Dein Ergebnis sind %u von %d erreichbaren Punkten!\n–> %s\n",
           answer_count*2, question_count*2, result);
}
