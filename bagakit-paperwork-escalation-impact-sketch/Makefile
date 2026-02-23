SKILL_NAME := bagakit-paperwork-escalation-impact-sketch
DIST_DIR ?= dist
BAGAKIT_HOME ?= $(HOME)/.bagakit
SKILL_DIR := $(BAGAKIT_HOME)/skills/$(SKILL_NAME)

.PHONY: check validate package-skill install-skill clean

check:
	bash scripts/validate-skill.sh

validate: check

package-skill:
	@out_dir="$(DIST_DIR)"; \
	  case "$$out_dir" in \
	    /*) ;; \
	    *) out_dir="$$PWD/$$out_dir" ;; \
	  esac; \
	  mkdir -p "$$out_dir"; \
	  artifact="$$out_dir/$(SKILL_NAME).skill"; \
	  rm -f "$$artifact"; \
	  zip -r "$$artifact" SKILL.md SKILL_PAYLOAD.json README.md reference gate scripts agents \
	    -x "*/__pycache__/*" "*.pyc" "*.pyo" >/dev/null; \
	  echo "packaged: $$artifact"

install-skill:
	rm -rf "$(SKILL_DIR)"
	mkdir -p "$(SKILL_DIR)"
	cp -R SKILL.md SKILL_PAYLOAD.json README.md reference gate scripts agents "$(SKILL_DIR)/"
	find "$(SKILL_DIR)/scripts" -type f -name "*.sh" -exec chmod +x {} +
	find "$(SKILL_DIR)/scripts" -type f -name "*.py" -exec chmod +x {} +
	@echo "installed: $(SKILL_DIR)"

clean:
	rm -rf dist
