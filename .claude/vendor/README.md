# Skills tiers installés dans ce projet

| Pack | Source | Licence | Installé où |
|---|---|---|---|
| humanizer 4.0.0 | https://github.com/blader/humanizer (b48c832) | MIT (`.claude/skills/humanizer/LICENSE`) | `.claude/skills/humanizer/` |
| aaron-marketing-skills 20.2.0 | https://github.com/aaron-he-zhu/aaron-marketing-skills (43c7163) | Apache-2.0 (`aaron-marketing-skills/LICENSE`) | 120 skills dans `.claude/skills/`, commandes dans `.claude/commands/aaron/`, fichiers partagés ici |
| geo-seo-claude | https://github.com/zubair-trabzada/geo-seo-claude (989cae0) | MIT (`.claude/skills/geo/LICENSE`) | `.claude/skills/geo/` et `geo-*`, agents dans `.claude/agents/` |

Choix d'installation :
- aaron-marketing-skills : skills seulement. Les hooks automatiques du plugin (scripts lancés à chaque commande et à chaque fichier modifié) ne sont pas activés. Leurs fichiers CLAUDE.md et AGENTS.md ont été retirés de la copie. Les liens entre skills ont été réécrits vers leur nouvel emplacement.
- geo-seo-claude : les chemins `~/.claude/skills/` pointent vers ce dépôt (`"$(git rev-parse --show-toplevel)"/.claude/skills/`). Pas d'environnement Python isolé : les scripts utilisent `python3` ; dépendances dans `.claude/skills/geo/requirements.txt`.
