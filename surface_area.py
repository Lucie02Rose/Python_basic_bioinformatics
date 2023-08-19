# contact_surface v.3.0
# Copyleft Martin Christen, 2013

from pymol import cmd, stored


def contact_surface(receptor, ligand, states=0):
    """
    AUTHOR
    Martin Christen

    DESCRIPTION
    This script calculates individual or global contact surfaces between a
    receptor molecule and a bundle of docked ligand structures (which have
    to be loaded into PyMOL as a multimodel object).

    The exact contact surface area values (in Angstrom^2) are printed to
    the screen and also appended to a file called contactareas.txt

    If only a single global contact surface is calculated, a selection
    named "contact" is created that includes all receptor atoms within
    3.9A of any ligand atom.

    USAGE
    contact_surface receptor, ligand, [states=0]

    PARAMETERS

    receptor (string)
    The name of the selection/object representing the receptor protein

    ligand (string)
    The name of the selection/object representing the ligand.
    Note that this may be another protein!

    states (integer)
    Calculate contact surface between the receptor and the first n states
    of the ligand. If states = 0 (default), the script calculates a global
    contact surface which takes  all possible ligand states into account.
    """
    # sanity check the number of states
    states = abs(int(states))

    # make sure all atoms within an object occlude one another
    cmd.flag('ignore', 'none')

    # use solvent-accessible surface with high sampling density
    cmd.set('dot_solvent', '1')
    cmd.set('dot_density', '3')

    # if the 'states' parameter = 0 create a superposition of all ligand states
    if states == 0:
        cmd.split_states(ligand)
        cmd.group('ligandtemp', ligand + "_*")
        cmd.create(ligand + "_all", 'ligandtemp')
        cmd.delete('ligandtemp')

        # create complex
        cmd.create('complextemp', ligand + "_all " + receptor)

        # measure area
        ligand_area = cmd.get_area(ligand + "_all")
        receptor_area = cmd.get_area(receptor)
        complex_area = cmd.get_area('complextemp')
        # normalize since the area is counted TWICE (once on receptor and once on ligand)
        contact_area = ((ligand_area + receptor_area) - complex_area) / 2
        # delete complex
        cmd.delete('complextemp')

        # create the contact surface
        cmd.select('contact', "(" + receptor + " and (" + ligand + "_all around 3.9))")

        # print contact surface area
        f = open('contactareas.txt', 'a')
        print
        "%s - %s : " % (receptor, ligand),
        print >> f, "%-s\t%-s\t" % (receptor, ligand),
        print >> f, "%-s" % (contact_area)
        print
        contact_area
        f.close()
        print
        "The GLOBAL contact area between " + receptor + " and " + ligand + " is (A^2):"
        print((ligand_area + receptor_area) - complex_area) / 2

    # If 'states' <> 0 calculate the contact areas to the first 'states' ligand states.
    # No individual contact surface objects are created to avoid overloading PyMOL.
    else:
        # create an object for each ligand state
        cmd.split_states(ligand)

        # sanity check: do not exceed that maximum number of states
        if states > cmd.count_states(ligand):
            states = cmd.count_states(ligand)

        # calculate contact surface area
        print
        "The contact areas between " + receptor + " and " + ligand + " [states 1 - " + str(states) + "] are (A^2):"
        # start looping
        for s in range(1, states + 1):
            # create complex
            cmd.create("tmp", ligand, s, 1)
            cmd.create('complextemp', "tmp " + receptor)
            # measure areas
            ligand_area = cmd.get_area('tmp')
            receptor_area = cmd.get_area(receptor)
            complex_area = cmd.get_area('complextemp')
            # normalize since the area is counted TWICE (once on receptor and once on ligand)
            contact_area = ((ligand_area + receptor_area) - complex_area) / 2
            # delete temporary files
            cmd.delete('tmp')
            cmd.delete(ligand + "_*")
            cmd.delete('complextemp')
            # print contact surface area
            f = open('contactareas.txt', 'a')
            print
            "%s - %s_%-5s: " % (receptor, ligand, s),
            print >> f, "%-s\t%-s_%-5s\t" % (receptor, ligand, s),
            print >> f, "%-s" % (contact_area)
            print
            contact_area
            f.close()


cmd.extend("contact_surface", contact_surface)