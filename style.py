
stil_frame = """
        QFrame{
        background-color: #E83C91;
        border-radius: 5px;
        }
"""



stil_buton1 = """
            QPushButton {
                background-color: transparent;
                border: none;
                border-radius: 25px;
            }
            QPushButton:hover {
                background-color: #FFC4C4;
                border-radius: 5px; /* Colturi rotunjite la hover */
            }
            QPushButton:pressed {
                background-color: #FFC4C4;}"""

stil_buton2 = """ 
    QPushButton {
        background-color: pink;
        border: none;
        border-radius: 5px;
        border: 2px solid #850E35;
    }
    QPushButton:hover {
        background-color: #EE6983;
        border-radius: 5px; 
        border: 2px solid #850E35;
    }
    QPushButton:pressed {
        background-color: #EE6983;
    }
"""

stil_list =     """
            /* 1. Stilul General al Cutiei (Lista) */
            QListWidget {
                background-color: #FFC4C4;  /* Un gri inchis pentru sidebar */
                color: #FFFFFF;             /* Text alb */
                border: 2px solid #FFC4C4;               /* Fara chenar exterior */
                font-family: Consolas;  
                border-radius: 5px;
                font-size: 14px;
                outline: none;              /* Scoate linia punctata cand dai click */
            }

            /* 2. Stilul fiecarui rand (Item) */
            QListWidget::item {
                padding: 10px;              /* Spatiere generoasa (aerisit) */
                border-bottom: 1px solid #444; /* O linie fina intre playlisturi */
                border-radius: 5px;
            }

            /* 3. Cand treci cu mouse-ul peste un rand (Hover) */
            QListWidget::item:hover {
                background-color: #3E3E3E;  /* Se lumineaza putin */
            }

            /* 4. Cand un playlist este SELECTAT (Active) */
            QListWidget::item:selected {
                background-color: #E83C91;  /* Rozul tau inchis */
                color: white;               /* Text alb */
                border-left: 5px solid #FF8FB7; /* O dunga roz deschis in stanga de efect */
            }
            
            
            
            /* 1. Canalul Principal (Vertical) */
    QScrollBar:vertical {
        border: none;
        background: #2b2b2b;    /* Acelasi fundal ca lista, ca sa para invizibil */
        width: 8px;             /* Foarte subtire */
        margin: 0px;            /* Fara margini */
        border-radius: 4px;
    }

    /* 2. "Manerul" (Partea de care tragi) */
    QScrollBar::handle:vertical {
        background: #555555;    /* Gri inchis */
        min-height: 20px;       /* Inaltime minima ca sa il poti apuca */
        border-radius: 4px;     /* Complet rotund */
    }

    /* 3. Efect cand pui mouse-ul pe maner */
    QScrollBar::handle:vertical:hover {
        background: #FF8FB7;    /* Se face ROZ cand vrei sa scrollezi! */
    }

    /* 4. Ascundem sagetile de sus/jos (add-line si sub-line) */
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        height: 0px;
        background: none;
        border: none;
    }

    /* 5. Ascundem partea de canal ramasa goala (add-page si sub-page) */
    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }
        """