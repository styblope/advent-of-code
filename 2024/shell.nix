let
  pkgs = import <nixpkgs> {};
in
  pkgs.mkShellNoCC {
    packages = with pkgs; [
      nodejs
      python312
      python312Packages.plotext
    ];
  }
